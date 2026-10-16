# -*- coding: utf-8 -*-
"""
Projeto ConectaUDF: redes sociais com grafos
Disciplina: Estrutura de Dados II (Unidade III - Grafos)

Parte 1: rede original com 6 usuários (Caderno do Estudante, seções 3 a 9).
Parte 2: desafio em grupo - rede ampliada (seção 10).
Execução: python conecta_udf.py
"""
from collections import deque
from itertools import combinations

# ---------------------------------------------------------------- Parte 1
rede = {
    "Ana": ["Bruno", "Carla"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe"],
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa"],
}


def metricas(grafo):
    """Retorna (n, arestas, densidade, graus) de um grafo simples não direcionado."""
    n = len(grafo)
    graus = {u: len(v) for u, v in grafo.items()}
    arestas = sum(graus.values()) // 2        # cada amizade é contada duas vezes
    densidade = (2 * arestas) / (n * (n - 1))
    return n, arestas, densidade, graus


def validar(grafo):
    """Confere a reciprocidade das amizades e a ausência de laços."""
    for u, amigos in grafo.items():
        assert u not in amigos, f"laço em {u}"
        assert len(set(amigos)) == len(amigos), f"aresta repetida em {u}"
        for v in amigos:
            assert u in grafo[v], f"amizade não recíproca: {u} - {v}"


def menor_caminho(grafo, origem, destino):
    """Busca em largura: devolve um caminho com o menor número de arestas."""
    fila, anterior = deque([origem]), {origem: None}
    while fila:
        atual = fila.popleft()
        if atual == destino:
            caminho = []
            while atual is not None:
                caminho.append(atual)
                atual = anterior[atual]
            return caminho[::-1]
        for v in grafo[atual]:
            if v not in anterior:
                anterior[v] = atual
                fila.append(v)
    return None


def todos_caminhos(grafo, origem, destino, tamanho):
    """Todos os caminhos simples com exatamente 'tamanho' arestas."""
    achados = []

    def busca(atual, caminho):
        if len(caminho) - 1 > tamanho:
            return
        if atual == destino:
            if len(caminho) - 1 == tamanho:
                achados.append(list(caminho))
            return
        for v in grafo[atual]:
            if v not in caminho:
                busca(v, caminho + [v])

    busca(origem, [origem])
    return achados


def recomendar(grafo, minimo=2):
    """Pares que ainda não são amigos, ordenados pela quantidade de amigos em comum."""
    sugestoes = []
    for a, b in combinations(sorted(grafo), 2):
        if b not in grafo[a]:
            comuns = sorted(set(grafo[a]) & set(grafo[b]))
            if len(comuns) >= minimo:
                sugestoes.append((len(comuns), a, b, comuns))
    return sorted(sugestoes, key=lambda s: (-s[0], s[1], s[2]))


def relatorio(titulo, grafo):
    n, arestas, dens, graus = metricas(grafo)
    print(f"=== {titulo} ===")
    for usuario, g in graus.items():
        print(f"{usuario} tem {g} conexoes")
    print("Total de usuarios:", n)
    print("Soma dos graus:", sum(graus.values()))
    print("Total de amizades:", arestas)
    print(f"Densidade: {dens:.2%} ({dens:.4f})")
    maior = max(graus.values())
    print("Mais conexoes:", ", ".join(u for u, g in graus.items() if g == maior),
          f"(grau {maior})")
    print()
    return dens


validar(rede)
dens_antes = relatorio("Rede original", rede)

print("Menor caminho Ana -> Felipe:", " -> ".join(menor_caminho(rede, "Ana", "Felipe")))
for c in todos_caminhos(rede, "Ana", "Felipe", 3):
    print("Caminho com 3 arestas:", " -> ".join(c))
print()

# ---------------------------------------------------------------- Parte 2
# Desafio em grupo: quatro novos usuários e seis novas amizades.
novos = ["Gabriela", "Hugo", "Iris", "Joana"]
novas_amizades = [
    ("Felipe", "Gabriela"),
    ("Gabriela", "Hugo"),
    ("Hugo", "Iris"),
    ("Iris", "Joana"),
    ("Joana", "Ana"),
    ("Hugo", "Diego"),
]

rede2 = {u: list(a) for u, a in rede.items()}
for u in novos:
    rede2[u] = []
for a, b in novas_amizades:
    rede2[a].append(b)
    rede2[b].append(a)

validar(rede2)
dens_depois = relatorio("Rede ampliada", rede2)
print(f"Densidade antes: {dens_antes:.2%} | depois: {dens_depois:.2%}")
print()

print("Sugestões de amizade (2 ou mais amigos em comum):")
for qtd, a, b, comuns in recomendar(rede2):
    print(f"  {a} e {b}: {qtd} em comum ({', '.join(comuns)})")
