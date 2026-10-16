# -*- coding: utf-8 -*-
"""Estrutura de dados da rede social ConectaUDF.

A rede é modelada como um **grafo simples não direcionado**: cada vértice é um
usuário e cada aresta é uma amizade (recíproca, sem laços e sem repetições).

A representação interna é uma lista de adjacência, ``dict[usuário, set[usuário]]``.
O uso de conjuntos (``set``) garante, por construção, que uma amizade nunca é
duplicada, e o método :meth:`RedeSocial.adicionar_amizade` registra a aresta nos
dois sentidos, de modo que a reciprocidade não depende de quem escreve os dados.

Complexidade: ``V`` é o número de usuários e ``E`` o de amizades.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations
from typing import Dict, FrozenSet, Iterable, List, Mapping, Optional, Set, Tuple

Usuario = str
Amizade = Tuple[Usuario, Usuario]
Caminho = List[Usuario]


@dataclass(frozen=True)
class Sugestao:
    """Sugestão de amizade entre dois usuários que ainda não são amigos."""

    usuario_a: Usuario
    usuario_b: Usuario
    amigos_em_comum: Tuple[Usuario, ...]

    @property
    def quantidade(self) -> int:
        """Quantidade de amigos em comum."""
        return len(self.amigos_em_comum)


class RedeSocial:
    """Grafo simples não direcionado que representa uma rede social."""

    def __init__(
        self,
        usuarios: Iterable[Usuario] = (),
        amizades: Iterable[Amizade] = (),
    ) -> None:
        self._adjacencia: Dict[Usuario, Set[Usuario]] = {}
        for usuario in usuarios:
            self.adicionar_usuario(usuario)
        for a, b in amizades:
            self.adicionar_amizade(a, b)

    # ------------------------------------------------------------ construção
    @classmethod
    def de_lista_de_adjacencia(cls, adjacencia: Mapping[Usuario, Iterable[Usuario]]) -> "RedeSocial":
        """Cria a rede a partir de uma lista de adjacência (formato do Caderno).

        Levanta ``ValueError`` se houver laço, amizade repetida na lista de um
        usuário, amigo inexistente ou amizade não recíproca.
        """
        rede = cls(usuarios=adjacencia)
        for usuario, amigos in adjacencia.items():
            amigos = list(amigos)
            if len(set(amigos)) != len(amigos):
                raise ValueError(f"amizade repetida na lista de {usuario!r}")
            for amigo in amigos:
                if amigo not in adjacencia:
                    raise ValueError(f"{amigo!r} (amigo de {usuario!r}) não é um usuário da rede")
                if usuario not in adjacencia[amigo]:
                    raise ValueError(f"amizade não recíproca: {usuario!r} -> {amigo!r}")
                rede.adicionar_amizade(usuario, amigo)
        return rede

    def adicionar_usuario(self, usuario: Usuario) -> None:
        """Adiciona um usuário sem amigos (operação idempotente)."""
        self._adjacencia.setdefault(usuario, set())

    def adicionar_amizade(self, usuario_a: Usuario, usuario_b: Usuario) -> None:
        """Cria a amizade (recíproca) entre dois usuários, criando-os se preciso."""
        if usuario_a == usuario_b:
            raise ValueError(f"um usuário não pode ser amigo de si mesmo: {usuario_a!r}")
        self.adicionar_usuario(usuario_a)
        self.adicionar_usuario(usuario_b)
        self._adjacencia[usuario_a].add(usuario_b)
        self._adjacencia[usuario_b].add(usuario_a)

    def copia(self) -> "RedeSocial":
        """Retorna uma cópia independente da rede."""
        nova = RedeSocial(usuarios=self._adjacencia)
        for usuario, amigos in self._adjacencia.items():
            for amigo in amigos:
                nova.adicionar_amizade(usuario, amigo)
        return nova

    # ---------------------------------------------------------- consultas básicas
    @property
    def usuarios(self) -> Tuple[Usuario, ...]:
        """Usuários na ordem em que foram inseridos."""
        return tuple(self._adjacencia)

    @property
    def numero_usuarios(self) -> int:
        """Ordem do grafo, ``|V|``."""
        return len(self._adjacencia)

    @property
    def numero_amizades(self) -> int:
        """Tamanho do grafo, ``|E|`` = soma dos graus ÷ 2 (cada aresta é contada duas vezes)."""
        return sum(self.graus().values()) // 2

    def amizades(self) -> List[Amizade]:
        """Lista cada amizade uma única vez, com os nomes em ordem alfabética."""
        return sorted(
            (a, b) for a, amigos in self._adjacencia.items() for b in amigos if a < b
        )

    def amigos(self, usuario: Usuario) -> Tuple[Usuario, ...]:
        """Amigos diretos de um usuário, em ordem alfabética."""
        return tuple(sorted(self._adjacencia[self._validar(usuario)]))

    def sao_amigos(self, usuario_a: Usuario, usuario_b: Usuario) -> bool:
        """Indica se existe a amizade entre os dois usuários."""
        return usuario_b in self._adjacencia[self._validar(usuario_a)]

    def amigos_em_comum(self, usuario_a: Usuario, usuario_b: Usuario) -> Tuple[Usuario, ...]:
        """Amigos comuns a dois usuários, em ordem alfabética."""
        comuns = self._adjacencia[self._validar(usuario_a)] & self._adjacencia[self._validar(usuario_b)]
        return tuple(sorted(comuns))

    # ---------------------------------------------------------------- métricas
    def grau(self, usuario: Usuario) -> int:
        """Grau: quantidade de conexões diretas do usuário."""
        return len(self._adjacencia[self._validar(usuario)])

    def graus(self) -> Dict[Usuario, int]:
        """Grau de cada usuário."""
        return {usuario: len(amigos) for usuario, amigos in self._adjacencia.items()}

    def usuarios_mais_conectados(self) -> Tuple[Usuario, ...]:
        """Usuários de maior grau (pode haver empate), em ordem alfabética."""
        graus = self.graus()
        if not graus:
            return ()
        maior = max(graus.values())
        return tuple(sorted(u for u, g in graus.items() if g == maior))

    def densidade(self) -> float:
        """Densidade ``D = 2E / (V(V-1))``; vale 0 quando há menos de dois usuários."""
        n = self.numero_usuarios
        if n < 2:
            return 0.0
        return (2 * self.numero_amizades) / (n * (n - 1))

    def coeficiente_de_agrupamento(self, usuario: Usuario) -> float:
        """Fração dos pares de amigos do usuário que também são amigos entre si."""
        amigos = self.amigos(usuario)
        if len(amigos) < 2:
            return 0.0
        triangulos = sum(1 for a, b in combinations(amigos, 2) if self.sao_amigos(a, b))
        return triangulos / (len(amigos) * (len(amigos) - 1) / 2)

    def centralidade_de_proximidade(self, usuario: Usuario) -> float:
        """Proximidade (closeness): o quão perto o usuário está, em média, dos demais.

        Para um grafo conexo vale ``(V-1) / soma das distâncias``; em grafos
        desconexos considera apenas os usuários alcançáveis (fórmula de
        Wasserman e Faust), como faz o NetworkX.
        """
        distancias = self._distancias(self._validar(usuario))
        alcancaveis = len(distancias) - 1
        total = sum(distancias.values())
        if alcancaveis == 0 or total == 0:
            return 0.0
        return (alcancaveis / total) * (alcancaveis / (self.numero_usuarios - 1))

    # ------------------------------------------------------------- caminhos
    def menor_caminho(self, origem: Usuario, destino: Usuario) -> Optional[Caminho]:
        """Um caminho com o menor número de arestas (busca em largura), ou ``None``.

        Complexidade ``O(V + E)``. Os vizinhos são visitados em ordem alfabética,
        o que torna o resultado determinístico.
        """
        self._validar(origem)
        self._validar(destino)
        anterior: Dict[Usuario, Optional[Usuario]] = {origem: None}
        fila = deque([origem])
        while fila:
            atual = fila.popleft()
            if atual == destino:
                break
            for vizinho in sorted(self._adjacencia[atual]):
                if vizinho not in anterior:
                    anterior[vizinho] = atual
                    fila.append(vizinho)
        if destino not in anterior:
            return None
        caminho: Caminho = []
        passo: Optional[Usuario] = destino
        while passo is not None:
            caminho.append(passo)
            passo = anterior[passo]
        return caminho[::-1]

    def distancia(self, origem: Usuario, destino: Usuario) -> Optional[int]:
        """Número de arestas do menor caminho, ou ``None`` se não houver caminho."""
        caminho = self.menor_caminho(origem, destino)
        return None if caminho is None else len(caminho) - 1

    def caminhos_minimos(self, origem: Usuario, destino: Usuario) -> List[Caminho]:
        """Todos os caminhos de comprimento mínimo entre dois usuários."""
        self._validar(origem)
        self._validar(destino)
        distancias = self._distancias(origem)
        if destino not in distancias:
            return []
        achados: List[Caminho] = []

        def percorrer(atual: Usuario, caminho: Caminho) -> None:
            if atual == destino:
                achados.append(caminho)
                return
            for vizinho in sorted(self._adjacencia[atual]):
                if distancias.get(vizinho) == distancias[atual] + 1:
                    percorrer(vizinho, caminho + [vizinho])

        percorrer(origem, [origem])
        return achados

    def componentes_conexos(self) -> List[FrozenSet[Usuario]]:
        """Conjuntos de usuários mutuamente alcançáveis, do maior para o menor."""
        visitados: Set[Usuario] = set()
        componentes: List[FrozenSet[Usuario]] = []
        for usuario in self._adjacencia:
            if usuario not in visitados:
                componente = frozenset(self._distancias(usuario))
                visitados |= componente
                componentes.append(componente)
        return sorted(componentes, key=lambda c: (-len(c), sorted(c)))

    def esta_conexa(self) -> bool:
        """Verdadeiro se todo usuário alcança todos os demais."""
        return self.numero_usuarios > 0 and len(self.componentes_conexos()) == 1

    def diametro(self) -> Optional[int]:
        """Maior distância entre dois usuários, ou ``None`` se a rede for desconexa."""
        if not self.esta_conexa():
            return None
        return max(max(self._distancias(u).values()) for u in self._adjacencia)

    # -------------------------------------------------------- recomendação
    def sugestoes_de_amizade(self, minimo_em_comum: int = 2) -> List[Sugestao]:
        """Pares que ainda não são amigos, ordenados por amigos em comum (maior primeiro)."""
        sugestoes = [
            Sugestao(a, b, comuns)
            for a, b in combinations(sorted(self._adjacencia), 2)
            if not self.sao_amigos(a, b)
            and len(comuns := self.amigos_em_comum(a, b)) >= minimo_em_comum
        ]
        return sorted(sugestoes, key=lambda s: (-s.quantidade, s.usuario_a, s.usuario_b))

    # ------------------------------------------------------------ auxiliares
    def _validar(self, usuario: Usuario) -> Usuario:
        if usuario not in self._adjacencia:
            raise KeyError(f"usuário inexistente: {usuario!r}")
        return usuario

    def _distancias(self, origem: Usuario) -> Dict[Usuario, int]:
        """Distância de ``origem`` a cada usuário alcançável (busca em largura)."""
        distancias = {origem: 0}
        fila = deque([origem])
        while fila:
            atual = fila.popleft()
            for vizinho in self._adjacencia[atual]:
                if vizinho not in distancias:
                    distancias[vizinho] = distancias[atual] + 1
                    fila.append(vizinho)
        return distancias

    def __repr__(self) -> str:
        return f"RedeSocial(usuarios={self.numero_usuarios}, amizades={self.numero_amizades})"
