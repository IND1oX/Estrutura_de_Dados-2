# Estrutura de Dados II — Grafos
## Unidade III — Desafios 5 e 7

Material elaborado com base no documento **Material do Estudante - Prática de Grafos**, da Unidade III.

---

## Desafio 5 — Isomorfismo

### 1. Ordem e tamanho

- **G:** \(V = \{1,2,3,4\}\), então a ordem é \(|V(G)|=4\). O conjunto possui 4 arestas, portanto \(|E(G)|=4\).
- **H:** \(V = \{a,b,c,d\}\), então a ordem é \(|V(H)|=4\). O conjunto possui 4 arestas, portanto \(|E(H)|=4\).

### 2. Grau dos vértices e sequência de graus

Em **G**, as arestas são \((1,2), (2,3), (3,4), (4,1)\).

| Vértice | Grau |
|---|---:|
| 1 | 2 |
| 2 | 2 |
| 3 | 2 |
| 4 | 2 |

Sequência de graus de G, em ordem não decrescente: **(2, 2, 2, 2)**.

Em **H**, as arestas são \((a,c), (c,b), (b,d), (d,a)\).

| Vértice | Grau |
|---|---:|
| a | 2 |
| b | 2 |
| c | 2 |
| d | 2 |

Sequência de graus de H, em ordem não decrescente: **(2, 2, 2, 2)**.

### 3. Tabela de correspondência

| Vértice em G | Correspondente em H |
|---|---|
| 1 | a |
| 2 | c |
| 3 | b |
| 4 | d |

### 4. Verificação das adjacências

A correspondência preserva todas as arestas:

| Aresta de G | Aresta correspondente em H | Preserva a adjacência? |
|---|---|---|
| (1, 2) | (a, c) | Sim |
| (2, 3) | (c, b) | Sim |
| (3, 4) | (b, d) | Sim |
| (4, 1) | (d, a) | Sim |

Cada aresta de G é transformada em uma aresta existente em H. A correspondência também utiliza cada vértice de H exatamente uma vez.

### 5. Conclusão e justificativa

**Sim, G e H são isomorfos.** Ambos possuem quatro vértices, quatro arestas e a mesma sequência de graus. Além disso, a correspondência \(1\to a\), \(2\to c\), \(3\to b\) e \(4\to d\) preserva todas as adjacências. Portanto, os grafos têm a mesma estrutura, mesmo que os vértices tenham rótulos diferentes.

### Reflexão: ter a mesma sequência de graus é suficiente para garantir isomorfismo?

**Não.** A sequência de graus igual é uma condição necessária, mas não suficiente. Por exemplo, um ciclo com seis vértices e um grafo formado por dois triângulos separados têm ambos a sequência de graus \((2,2,2,2,2,2)\), mas não são isomorfos: no ciclo todos os vértices pertencem a uma única componente conectada; nos dois triângulos existem duas componentes separadas.

---

## Desafio 7 — Sequência de graus

A sequência solicitada é **(1, 1, 2, 3, 3, 4, 4, 6)**. Vamos construir um grafo simples com os vértices A, B, C, D, E, F, G e H.

### 1. Conjunto de vértices

\[
V = \{A,B,C,D,E,F,G,H\}
\]

### 2. Conjunto de arestas construído

\[
\begin{aligned}
E = \{ &(A,B), (A,C), (A,D), (A,E), (A,F), (A,G),\\
       &(B,C), (B,D), (B,E), (C,D), (C,E), (F,H) \}
\end{aligned}
\]

Não há laços nem arestas paralelas, portanto o grafo é simples.

### 3. Grau de cada vértice

| Vértice | Vizinhos | Grau obtido |
|---|---|---:|
| A | B, C, D, E, F, G | 6 |
| B | A, C, D, E | 4 |
| C | A, B, D, E | 4 |
| D | A, B, C | 3 |
| E | A, B, C | 3 |
| F | A, H | 2 |
| G | A | 1 |
| H | F | 1 |

### 4. Sequência obtida

Ordenando os graus em ordem não decrescente, obtemos:

**(1, 1, 2, 3, 3, 4, 4, 6)**

A sequência obtida é igual à sequência solicitada.

### 5. Soma dos graus e número de arestas

- **Soma dos graus:** \(6+4+4+3+3+2+1+1=24\).
- **Número de arestas:** \(|E|=12\).

### 6. Verificação

Pelo lema do aperto de mãos, a soma dos graus de um grafo não dirigido é igual ao dobro do número de arestas:

\[
\sum_{v\in V}\deg(v)=2|E|
\]

Substituindo os valores:

\[
24=2\times12=24
\]

**A igualdade é verdadeira.** Logo, a soma dos graus confere com o dobro do número de arestas, e a construção atende à sequência proposta.

---

## Referência

GOMES, Paulo César Rodacki. **Grafos: conceitos fundamentais, algoritmos e aplicações**. Blumenau: Editora IFC, 2022. Material de apoio indicado no documento da Unidade III.
