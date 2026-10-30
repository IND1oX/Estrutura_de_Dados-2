# -*- coding: utf-8 -*-
"""Formatação dos resultados em texto.

As funções deste módulo apenas montam *strings*; quem decide imprimir é o
programa principal. Assim a apresentação fica separada do cálculo e pode ser
testada sem capturar a saída padrão.
"""
from __future__ import annotations

from typing import List, Optional

from .grafo import Caminho, RedeSocial


def formatar_caminho(caminho: Optional[Caminho]) -> str:
    """``Ana → Bruno → Diego`` ou um aviso quando não há caminho."""
    return " → ".join(caminho) if caminho else "(sem caminho)"


def formatar_relatorio(titulo: str, rede: RedeSocial) -> str:
    """Relatório com graus, número de amizades, densidade e demais métricas."""
    graus = rede.graus()
    diametro = rede.diametro()
    linhas: List[str] = [f"=== {titulo} ==="]
    linhas.append(f"{'Usuário':<10}{'Grau':>5}{'Proximidade':>13}{'Agrupamento':>13}")
    for usuario in rede.usuarios:
        linhas.append(
            f"{usuario:<10}{graus[usuario]:>5}"
            f"{rede.centralidade_de_proximidade(usuario):>13.3f}"
            f"{rede.coeficiente_de_agrupamento(usuario):>13.3f}"
        )
    maior = max(graus.values())
    linhas += [
        f"Total de usuários: {rede.numero_usuarios}",
        f"Soma dos graus: {sum(graus.values())}",
        f"Total de amizades: {rede.numero_amizades}",
        f"Densidade: {rede.densidade():.2%} ({rede.densidade():.4f})",
        f"Mais conectados (grau {maior}): {', '.join(rede.usuarios_mais_conectados())}",
        f"Componentes conexos: {len(rede.componentes_conexos())}",
        f"Diâmetro: {diametro if diametro is not None else 'indefinido (rede desconexa)'}",
    ]
    return "\n".join(linhas)


def formatar_sugestoes(rede: RedeSocial, minimo_em_comum: int = 2) -> str:
    """Lista de sugestões de amizade por amigos em comum."""
    sugestoes = rede.sugestoes_de_amizade(minimo_em_comum)
    if not sugestoes:
        return "Nenhuma sugestão de amizade."
    return "\n".join(
        f"{s.usuario_a} e {s.usuario_b}: {s.quantidade} em comum ({', '.join(s.amigos_em_comum)})"
        for s in sugestoes
    )
