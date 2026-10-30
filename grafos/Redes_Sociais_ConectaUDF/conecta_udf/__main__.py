# -*- coding: utf-8 -*-
"""Programa principal do mini projeto ConectaUDF.

Execução (a partir da pasta ``Redes_Sociais_ConectaUDF``):

    python -m conecta_udf
    python -m conecta_udf --origem Ana --destino Felipe
"""
from __future__ import annotations

import argparse
from typing import Optional, Sequence

from .dados import rede_ampliada, rede_original
from .relatorio import formatar_caminho, formatar_relatorio, formatar_sugestoes


def _argumentos(argv: Optional[Sequence[str]]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Mini projeto ConectaUDF: redes sociais com grafos.")
    parser.add_argument("--origem", default="Ana", help="usuário de origem do caminho (padrão: Ana)")
    parser.add_argument("--destino", default="Felipe", help="usuário de destino do caminho (padrão: Felipe)")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _argumentos(argv)
    original, ampliada = rede_original(), rede_ampliada()

    print(formatar_relatorio("Rede original", original))
    print()

    try:
        caminhos = original.caminhos_minimos(args.origem, args.destino)
    except KeyError as erro:
        print(f"Erro: {erro.args[0]}")
        return 1
    print(f"Caminhos mínimos de {args.origem} a {args.destino} "
          f"({original.distancia(args.origem, args.destino)} arestas):")
    for caminho in caminhos:
        print("  " + formatar_caminho(caminho))
    print()

    print(formatar_relatorio("Rede ampliada (desafio em grupo)", ampliada))
    print()
    print(f"Densidade antes: {original.densidade():.2%} | depois: {ampliada.densidade():.2%}")
    print()
    print("Sugestões de amizade (2 ou mais amigos em comum):")
    print(formatar_sugestoes(ampliada))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
