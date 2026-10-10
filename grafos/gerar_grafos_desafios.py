# -*- coding: utf-8 -*-
"""
Desafios 5 e 7 - Grafos (Unidade III) - Estrutura de Dados II.

Gera as imagens e confere os resultados com Python/NetworkX
(plataforma prevista no material: "Google Colab com Python e NetworkX").

Uso:  python gerar_grafos_desafios.py
Saída: imagens/desafio5-isomorfismo.png e imagens/desafio7-sequencia-graus.png
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx

PASTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imagens")
os.makedirs(PASTA, exist_ok=True)

# ---------------------------------------------------------------- Desafio 5
G = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1)])
H = nx.Graph([("a", "c"), ("c", "b"), ("b", "d"), ("d", "a")])
mapa = {1: "a", 2: "c", 3: "b", 4: "d"}          # G -> H

print("Desafio 5")
print("  ordem  G, H:", G.number_of_nodes(), H.number_of_nodes())
print("  tamanho G, H:", G.number_of_edges(), H.number_of_edges())
print("  graus G:", sorted(dict(G.degree()).values()),
      "| graus H:", sorted(dict(H.degree()).values()))
for u, v in G.edges():
    ok = H.has_edge(mapa[u], mapa[v])
    print(f"  ({u},{v}) -> ({mapa[u]},{mapa[v]}) em H? {ok}")
    assert ok
assert nx.is_isomorphic(G, H)
print("  isomorfos:", nx.is_isomorphic(G, H))

cores = {1: "#4F8FE8", 2: "#E8954F", 3: "#4FBF6B", 4: "#C85FD6"}
quadrado = {1: (0, 1), 2: (1, 1), 3: (1, 0), 4: (0, 0)}
# H desenhado de outra forma (losango) para mostrar que o desenho não importa
losango = {"a": (0.5, 1.1), "c": (1.1, 0.5), "b": (0.5, -0.1), "d": (-0.1, 0.5)}
inv = {v: k for k, v in mapa.items()}

fig, ax = plt.subplots(1, 2, figsize=(10, 4.8))
nx.draw(G, quadrado, ax=ax[0], with_labels=True, node_size=1300,
        node_color=[cores[n] for n in G.nodes()], font_color="white",
        font_weight="bold", font_size=14, width=2.2, edge_color="#333")
ax[0].set_title("Grafo G\nV={1,2,3,4}  E={(1,2),(2,3),(3,4),(4,1)}", fontsize=10)
nx.draw(H, losango, ax=ax[1], with_labels=True, node_size=1300,
        node_color=[cores[inv[n]] for n in H.nodes()], font_color="white",
        font_weight="bold", font_size=14, width=2.2, edge_color="#333")
ax[1].set_title("Grafo H\nV={a,b,c,d}  E={(a,c),(c,b),(b,d),(d,a)}", fontsize=10)
for a in ax:
    a.set_xlim(-0.5, 1.5); a.set_ylim(-0.5, 1.5)
fig.suptitle("Desafio 5 - G e H são isomorfos (mesma cor = vértices correspondentes: "
             "1→a, 2→c, 3→b, 4→d)", fontsize=10.5, y=1.04)
fig.savefig(os.path.join(PASTA, "desafio5-isomorfismo.png"), dpi=170,
            bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- Desafio 7
arestas = [("A", "B"), ("A", "C"), ("A", "D"), ("A", "E"), ("A", "F"), ("A", "G"),
           ("B", "C"), ("B", "D"), ("B", "E"), ("C", "D"), ("C", "H"), ("E", "F")]
S = nx.Graph(arestas)
graus = dict(sorted(S.degree()))
seq = sorted(graus.values())

print("\nDesafio 7")
print("  graus:", graus)
print("  sequência:", tuple(seq))
print("  soma dos graus:", sum(seq), "| arestas:", S.number_of_edges(),
      "| 2x arestas:", 2 * S.number_of_edges())
assert seq == [1, 1, 2, 3, 3, 4, 4, 6]
assert sum(seq) == 2 * S.number_of_edges()
assert nx.number_of_selfloops(S) == 0          # grafo simples: sem laços
# (nx.Graph já impede arestas paralelas)

ordem = ["A", "G", "F", "E", "B", "C", "H", "D"]
pos = nx.circular_layout(ordem)
fig, ax = plt.subplots(figsize=(6.4, 6))
nx.draw_networkx_edges(S, pos, ax=ax, width=2.2, edge_color="#475569")
nx.draw_networkx_nodes(S, pos, ax=ax, node_size=1700, node_color="#4F8FE8")
nx.draw_networkx_labels(S, pos, ax=ax, font_color="white", font_weight="bold",
                        labels={v: f"{v}\ngrau {graus[v]}" for v in S}, font_size=9)
ax.set_title("Desafio 7 - grafo simples com sequência de graus (1, 1, 2, 3, 3, 4, 4, 6)",
             fontsize=10)
ax.margins(0.15); ax.axis("off")
fig.savefig(os.path.join(PASTA, "desafio7-sequencia-graus.png"), dpi=170,
            bbox_inches="tight")
plt.close(fig)
print("\nImagens salvas em", PASTA)
