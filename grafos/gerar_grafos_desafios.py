# -*- coding: utf-8 -*-
"""
Desafios 5 e 7 - Grafos (Unidade III) - Estrutura de Dados II.

Os grafos foram construídos no Miro (quadro "Grafos - Desafios 5 e 7 (ED II)",
https://miro.com/app/board/uXjVEbl3LCk=/). Como o Miro não exporta PNG por
automação, este script redesenha os mesmos quadros (mesmas posições, cores e
textos) em arquivos PNG para o GitHub e confere os resultados com NetworkX.

Uso:  python gerar_grafos_desafios.py
Saída: imagens/desafio5-isomorfismo.png e imagens/desafio7-sequencia-graus.png
"""
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import networkx as nx

PASTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imagens")
os.makedirs(PASTA, exist_ok=True)

AZUL, AZUL_CLARO, VERDE = "#659df2", "#c6dcff", "#2dc75c"
TINTA, CORPO, LINHA, PAINEL, PAINEL_TXT = "#1a1a1a", "#595959", "#313131", "#f0f5fd", "#305bab"

# ----------------------------------------------------------------- conferência
G = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1)])
H = nx.Graph([("a", "c"), ("c", "b"), ("b", "d"), ("d", "a")])
mapa = {1: "a", 2: "c", 3: "b", 4: "d"}
assert all(H.has_edge(mapa[u], mapa[v]) for u, v in G.edges())
assert nx.is_isomorphic(G, H)
assert sorted(dict(G.degree()).values()) == sorted(dict(H.degree()).values()) == [2, 2, 2, 2]

ARESTAS7 = [("A", "B"), ("A", "C"), ("A", "D"), ("A", "E"), ("A", "F"), ("A", "G"),
            ("B", "C"), ("B", "D"), ("B", "E"), ("C", "D"), ("C", "H"), ("E", "F")]
S = nx.Graph(ARESTAS7)
graus = dict(sorted(S.degree()))
assert sorted(graus.values()) == [1, 1, 2, 3, 3, 4, 4, 6]
assert sum(graus.values()) == 2 * S.number_of_edges() == 24
assert nx.number_of_selfloops(S) == 0


# ----------------------------------------------------------------- desenho
def quadro(largura, altura):
    fig = plt.figure(figsize=(largura / 100, altura / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, largura)
    ax.set_ylim(altura, 0)           # y para baixo, como no Miro
    ax.axis("off")
    return fig, ax


def aresta(ax, p, q, r):
    (x1, y1), (x2, y2) = p, q
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    ax.plot([x1 + ux * r, x2 - ux * r], [y1 + uy * r, y2 - uy * r],
            color=LINHA, lw=3, solid_capstyle="round", zorder=1)


def vertice(ax, pos, r, cor, rotulo, fs):
    ax.add_patch(Circle(pos, r, color=cor, zorder=2))
    ax.text(*pos, rotulo, ha="center", va="center", fontsize=fs,
            fontweight="bold", color=TINTA, zorder=3, linespacing=1.3)


def painel(ax, x, y, w, h, texto, fs=15, topo=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=12",
                                color=PAINEL, zorder=1))
    if topo:
        ax.text(x + 24, y + 24, texto, ha="left", va="top", fontsize=fs,
                color=PAINEL_TXT, linespacing=1.55)
    else:
        ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs,
                fontweight="bold", color=PAINEL_TXT, linespacing=1.5)


def desafio5():
    fig, ax = quadro(1400, 780)
    ax.text(64, 64, "Desafio 5: G e H são isomorfos", fontsize=25, fontweight="bold",
            color=TINTA, va="top")
    ax.text(64, 137, "Ordem 4 e tamanho 4 nos dois grafos. Sequência de graus (2, 2, 2, 2) "
            "em G e em H. Todas as arestas de G têm imagem em H.", fontsize=13,
            color=CORPO, va="top")
    ax.text(150, 245, "Grafo G\nV={1,2,3,4}  E={(1,2),(2,3),(3,4),(4,1)}", fontsize=15,
            fontweight="bold", color=TINTA, va="top", linespacing=1.3)
    ax.text(800, 230, "Grafo H\nV={a,b,c,d}  E={(a,c),(c,b),(b,d),(d,a)}", fontsize=15,
            fontweight="bold", color=TINTA, va="top", linespacing=1.3)
    pg = {1: (190, 400), 2: (450, 400), 3: (450, 640), 4: (190, 640)}
    ph = {"a": (1050, 370), "c": (1230, 520), "b": (1050, 670), "d": (870, 520)}
    for u, v in G.edges():
        aresta(ax, pg[u], pg[v], 45)
    for u, v in H.edges():
        aresta(ax, ph[u], ph[v], 45)
    for n, p in pg.items():
        vertice(ax, p, 45, AZUL, str(n), 15)
    for n, p in ph.items():
        vertice(ax, p, 45, VERDE, n, 15)
    painel(ax, 560, 410, 240, 220, "Correspondência\n1 → a\n2 → c\n3 → b\n4 → d")
    fig.savefig(os.path.join(PASTA, "desafio5-isomorfismo.png"))
    plt.close(fig)


def desafio7():
    fig, ax = quadro(1700, 960)
    ax.text(64, 64, "Desafio 7: grafo simples com graus (1, 1, 2, 3, 3, 4, 4, 6)",
            fontsize=25, fontweight="bold", color=TINTA, va="top")
    ax.text(64, 137, "Oito vértices, 12 arestas, sem laços e sem arestas paralelas. "
            "Em cada vértice aparece o seu grau.", fontsize=13, color=CORPO, va="top")
    ordem = ["A", "G", "F", "E", "B", "C", "H", "D"]
    pos = {}
    for k, v in enumerate(ordem):
        a = math.radians(-90 + 45 * k)
        pos[v] = (round(520 + 300 * math.cos(a)), round(500 + 300 * math.sin(a)) + 60)
    for u, v in ARESTAS7:
        aresta(ax, pos[u], pos[v], 62)
    for v, p in pos.items():
        vertice(ax, p, 62, AZUL if graus[v] >= 4 else AZUL_CLARO,
                f"{v}\ngrau {graus[v]}", 13)
    texto = ("Vértices e graus\nA: 6 (B, C, D, E, F, G)\nB: 4 (A, C, D, E)\n"
             "C: 4 (A, B, D, H)\nD: 3 (A, B, C)\nE: 3 (A, B, F)\nF: 2 (A, E)\n"
             "G: 1 (A)\nH: 1 (C)\n\nSequência obtida: (1, 1, 2, 3, 3, 4, 4, 6)\n"
             "Soma dos graus: 24\nArestas: 12, e 24 = 2 × 12")
    painel(ax, 1020, 260, 580, 560, texto, fs=14, topo=True)
    fig.savefig(os.path.join(PASTA, "desafio7-sequencia-graus.png"))
    plt.close(fig)


if __name__ == "__main__":
    desafio5()
    desafio7()
    print("Conferências OK. Imagens salvas em", PASTA)
