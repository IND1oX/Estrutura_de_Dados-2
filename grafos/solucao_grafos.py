# -*- coding: utf-8 -*-
"""Conectividade de uma rede fictícia de cidades com BFS e DFS.

Atividade de Estrutura de Dados II (Grafos, BFS e DFS). O estudo de caso é
motivado por uma pane de GPS no Aeroporto de Brasília (G1, 22 set. 2026), mas
a rede, as conexões e os bloqueios aqui são FICTÍCIOS: o programa estuda
conectividade e algoritmos de busca, e não serve para planejar voos reais.

Pergunta de pesquisa
    Quantas conexões da rede precisam ser bloqueadas para que Brasília deixe
    de alcançar Curitiba, e como BFS e DFS se comportam a cada bloqueio?

Modelo
    Grafo simples não dirigido, não ponderado. Vértices são cidades e arestas
    são ligações permitidas nos dois sentidos. A representação é uma lista de
    adjacência (``dict[str, list[str]]``). As listas preservam a ordem de
    inserção, pois a ordem dos vizinhos influencia o caminho achado pela DFS.

Complexidade: ``V`` é o número de cidades e ``E`` o de conexões.
    BFS e DFS: O(V + E) tempo, O(V) memória (cada caminho guarda até V nomes).

Uso (dentro desta pasta)
    python solucao_grafos.py
    python solucao_grafos.py --origem Brasília --destino "Porto Alegre"
    python solucao_grafos.py --bloquear "Goiânia-São Paulo" --bloquear "Brasília-Goiânia"
"""
from __future__ import annotations

import argparse
import sys
from collections import deque
from dataclasses import dataclass
from itertools import combinations
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

Cidade = str
Conexao = Tuple[Cidade, Cidade]
Caminho = List[Cidade]

ORIGEM_PADRAO = "Brasília"
DESTINO_PADRAO = "Curitiba"

# Conexões fictícias da rede (ordem de inserção = ordem dos vizinhos).
CONEXOES_PADRAO: Tuple[Conexao, ...] = (
    ("Brasília", "Goiânia"),           # vizinhas no Centro-Oeste
    ("Brasília", "Belo Horizonte"),    # eixo Centro-Oeste/Sudeste
    ("Goiânia", "Campo Grande"),       # corredor Centro-Oeste
    ("Goiânia", "São Paulo"),          # ligação com o principal polo do Sudeste
    ("Belo Horizonte", "Rio de Janeiro"),
    ("Belo Horizonte", "São Paulo"),
    ("Rio de Janeiro", "São Paulo"),   # eixo Rio-São Paulo
    ("São Paulo", "Curitiba"),         # ligação direta com o Sul
    ("Campo Grande", "Porto Alegre"),  # rota alternativa pelo interior
    ("Porto Alegre", "Florianópolis"),
    ("Florianópolis", "Curitiba"),     # acesso a Curitiba pelo litoral sul
)


class CidadeInexistenteError(KeyError):
    """Levantada quando se consulta uma cidade que não está na rede."""


class RedeDeCidades:
    """Grafo simples não dirigido com lista de adjacência."""

    def __init__(self, conexoes: Iterable[Conexao] = ()) -> None:
        self._adjacencia: Dict[Cidade, List[Cidade]] = {}
        for a, b in conexoes:
            self.adicionar_conexao(a, b)

    # ------------------------------------------------------------ construção
    def adicionar_conexao(self, a: Cidade, b: Cidade) -> None:
        """Cria a conexão nos dois sentidos; rejeita laço e ignora repetição."""
        if a == b:
            raise ValueError(f"uma cidade não pode se conectar a si mesma: {a!r}")
        self._adjacencia.setdefault(a, [])
        self._adjacencia.setdefault(b, [])
        if b not in self._adjacencia[a]:
            self._adjacencia[a].append(b)
            self._adjacencia[b].append(a)

    def copia(self) -> "RedeDeCidades":
        """Cópia independente: alterá-la nunca modifica a rede original."""
        nova = RedeDeCidades()
        nova._adjacencia = {c: v.copy() for c, v in self._adjacencia.items()}
        return nova

    def com_bloqueio(self, a: Cidade, b: Cidade) -> "RedeDeCidades":
        """Nova rede sem a conexão ``a``–``b`` (a original não é alterada)."""
        self._validar(a)
        self._validar(b)
        nova = self.copia()
        if b in nova._adjacencia[a]:
            nova._adjacencia[a].remove(b)
            nova._adjacencia[b].remove(a)
        return nova

    # ------------------------------------------------------------- consultas
    @property
    def cidades(self) -> Tuple[Cidade, ...]:
        return tuple(self._adjacencia)

    def vizinhas(self, cidade: Cidade) -> Tuple[Cidade, ...]:
        return tuple(self._adjacencia[self._validar(cidade)])

    def conexoes(self) -> List[Conexao]:
        """Cada conexão uma única vez, na ordem de cadastro."""
        vistas = set()
        resultado: List[Conexao] = []
        for a, vizinhas in self._adjacencia.items():
            for b in vizinhas:
                if (b, a) not in vistas:
                    vistas.add((a, b))
                    resultado.append((a, b))
        return resultado

    def grau(self, cidade: Cidade) -> int:
        return len(self._adjacencia[self._validar(cidade)])

    # ------------------------------------------------------------ algoritmos
    def bfs(self, origem: Cidade, destino: Cidade) -> Optional[Caminho]:
        """Busca em largura (fila FIFO): caminho com o menor número de arestas."""
        self._validar(origem)
        self._validar(destino)
        fila = deque([(origem, [origem])])
        visitados = {origem}
        while fila:
            atual, caminho = fila.popleft()
            if atual == destino:
                return caminho
            for vizinha in self._adjacencia[atual]:
                if vizinha not in visitados:
                    visitados.add(vizinha)
                    fila.append((vizinha, caminho + [vizinha]))
        return None

    def dfs(self, origem: Cidade, destino: Cidade) -> Optional[Caminho]:
        """Busca em profundidade (pilha LIFO): um caminho qualquer, não o menor."""
        self._validar(origem)
        self._validar(destino)
        pilha = [(origem, [origem])]
        visitados = set()
        while pilha:
            atual, caminho = pilha.pop()
            if atual in visitados:
                continue
            visitados.add(atual)
            if atual == destino:
                return caminho
            # reversed: a primeira vizinha da lista é a primeira a sair da pilha
            for vizinha in reversed(self._adjacencia[atual]):
                if vizinha not in visitados:
                    pilha.append((vizinha, caminho + [vizinha]))
        return None

    def conjuntos_de_corte(self, origem: Cidade, destino: Cidade,
                           tamanho: int) -> List[Tuple[Conexao, ...]]:
        """Conjuntos de ``tamanho`` conexões cujo bloqueio isola origem e destino.

        Força bruta sobre as combinações de conexões (adequada a redes pequenas).
        Só considera conjuntos mínimos: nenhuma das conexões é dispensável.
        """
        if self.bfs(origem, destino) is None:
            return []
        achados = []
        for grupo in combinations(self.conexoes(), tamanho):
            rede = self
            for a, b in grupo:
                rede = rede.com_bloqueio(a, b)
            if rede.bfs(origem, destino) is not None:
                continue
            if any(self._sem(grupo, c).bfs(origem, destino) is None
                   for c in grupo):
                continue  # um subconjunto já isolava: o conjunto não é mínimo
            achados.append(grupo)
        return achados

    def _sem(self, grupo: Sequence[Conexao], dispensada: Conexao) -> "RedeDeCidades":
        rede = self
        for c in grupo:
            if c != dispensada:
                rede = rede.com_bloqueio(*c)
        return rede

    # ------------------------------------------------------------ auxiliares
    def _validar(self, cidade: Cidade) -> Cidade:
        if cidade not in self._adjacencia:
            raise CidadeInexistenteError(cidade)
        return cidade

    def __repr__(self) -> str:
        return f"RedeDeCidades(cidades={len(self._adjacencia)}, conexoes={len(self.conexoes())})"


# --------------------------------------------------------------- apresentação
def arestas(caminho: Optional[Caminho]) -> Optional[int]:
    """Quantidade de arestas de um caminho (``None`` se não há caminho)."""
    return None if caminho is None else len(caminho) - 1


def formatar_caminho(caminho: Optional[Caminho]) -> str:
    if caminho is None:
        return "sem caminho"
    return f"{' → '.join(caminho)} ({len(caminho) - 1} arestas)"


def relatorio_cenario(nome: str, rede: RedeDeCidades, origem: Cidade, destino: Cidade) -> str:
    por_bfs, por_dfs = rede.bfs(origem, destino), rede.dfs(origem, destino)
    return "\n".join([
        f"Cenário: {nome}",
        f"  BFS: {formatar_caminho(por_bfs)}",
        f"  DFS: {formatar_caminho(por_dfs)}",
    ])


def _ler_bloqueio(texto: str) -> Conexao:
    partes = [p.strip() for p in texto.split("-")]
    if len(partes) != 2 or not all(partes):
        raise argparse.ArgumentTypeError(
            f"use o formato 'CidadeA-CidadeB' (recebido: {texto!r})")
    return partes[0], partes[1]


def _perguntar(rede: RedeDeCidades, rotulo: str, padrao: Cidade) -> Cidade:
    """Lê uma cidade do teclado, repetindo até o nome existir na rede."""
    while True:
        try:
            resposta = input(f"{rotulo} [{padrao}]: ").strip() or padrao
        except EOFError:
            return padrao
        if resposta in rede.cidades:
            return resposta
        print(f"Cidade inexistente: {resposta!r}. Opções: {', '.join(rede.cidades)}")


def _argumentos(argv: Optional[Sequence[str]]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="BFS e DFS em uma rede fictícia de cidades.")
    parser.add_argument("--origem", help=f"cidade de origem (padrão: {ORIGEM_PADRAO})")
    parser.add_argument("--destino", help=f"cidade de destino (padrão: {DESTINO_PADRAO})")
    parser.add_argument("--bloquear", action="append", type=_ler_bloqueio, default=[],
                        metavar="A-B", help="conexão a bloquear, ex.: Goiânia-São Paulo (repetível)")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _argumentos(argv)
    rede = RedeDeCidades(CONEXOES_PADRAO)

    interativo = args.origem is None and args.destino is None and sys.stdin.isatty()
    origem = args.origem or (_perguntar(rede, "Origem", ORIGEM_PADRAO) if interativo else ORIGEM_PADRAO)
    destino = args.destino or (_perguntar(rede, "Destino", DESTINO_PADRAO) if interativo else DESTINO_PADRAO)

    try:
        rede.vizinhas(origem)   # valida os nomes antes de imprimir qualquer coisa
        rede.vizinhas(destino)
        print(f"Rede: {len(rede.cidades)} cidades e {len(rede.conexoes())} conexões (fictícias)")
        print(f"Trajeto: {origem} → {destino}\n")
        print(relatorio_cenario("rede completa", rede, origem, destino))

        if args.bloquear:
            bloqueada = rede
            for a, b in args.bloquear:
                bloqueada = bloqueada.com_bloqueio(a, b)
            nome = "bloqueio de " + ", ".join(f"{a}–{b}" for a, b in args.bloquear)
            print()
            print(relatorio_cenario(nome, bloqueada, origem, destino))
        else:
            for a, b in (("Goiânia", "São Paulo"), ("São Paulo", "Curitiba")):
                print()
                print(relatorio_cenario(f"bloqueio de {a}–{b}",
                                        rede.com_bloqueio(a, b), origem, destino))
            print("\nConjuntos mínimos de 2 conexões que isolam os extremos:")
            cortes = rede.conjuntos_de_corte(origem, destino, 2)
            if not cortes:
                print("  nenhum")
            for grupo in cortes:
                print("  " + " e ".join(f"{a}–{b}" for a, b in grupo))
    except CidadeInexistenteError as erro:
        print(f"Erro: cidade inexistente: {erro.args[0]!r}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
