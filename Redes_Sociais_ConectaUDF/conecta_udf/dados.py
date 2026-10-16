# -*- coding: utf-8 -*-
"""Dados do projeto ConectaUDF (Caderno do Estudante, seções 3 e 10).

Os dados ficam separados da lógica do grafo: para alterar a rede basta editar
as constantes abaixo, sem tocar na classe :class:`~conecta_udf.grafo.RedeSocial`.
"""
from __future__ import annotations

from typing import Tuple

from .grafo import Amizade, RedeSocial, Usuario

USUARIOS_ORIGINAIS: Tuple[Usuario, ...] = ("Ana", "Bruno", "Carla", "Diego", "Elisa", "Felipe")

AMIZADES_ORIGINAIS: Tuple[Amizade, ...] = (
    ("Ana", "Bruno"),
    ("Ana", "Carla"),
    ("Bruno", "Carla"),
    ("Bruno", "Diego"),
    ("Carla", "Elisa"),
    ("Diego", "Elisa"),
    ("Diego", "Felipe"),
    ("Elisa", "Felipe"),
)

# Desafio em grupo: quatro usuários fictícios e seis novas amizades.
NOVOS_USUARIOS: Tuple[Usuario, ...] = ("Gabriela", "Hugo", "Iris", "Joana")

NOVAS_AMIZADES: Tuple[Amizade, ...] = (
    ("Felipe", "Gabriela"),
    ("Gabriela", "Hugo"),
    ("Hugo", "Iris"),
    ("Iris", "Joana"),
    ("Joana", "Ana"),
    ("Hugo", "Diego"),
)


def rede_original() -> RedeSocial:
    """Rede com os seis usuários e as oito amizades do Caderno."""
    return RedeSocial(USUARIOS_ORIGINAIS, AMIZADES_ORIGINAIS)


def rede_ampliada() -> RedeSocial:
    """Rede original acrescida dos usuários e das amizades do desafio em grupo."""
    rede = rede_original()
    for usuario in NOVOS_USUARIOS:
        rede.adicionar_usuario(usuario)
    for a, b in NOVAS_AMIZADES:
        rede.adicionar_amizade(a, b)
    return rede
