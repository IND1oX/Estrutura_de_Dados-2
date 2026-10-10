# Desafios 5 e 7 — Grafos (Resolução)

**Disciplina:** Estrutura de Dados II  
**Unidade III:** Grafos  
**Professora:** Kadidja Valéria  
**Estudante:** Gustavo Alves  
**Material:** *Material do Estudante — Desafios 5 e 7*  
**Plataforma:** Miro (quadro: https://miro.com/app/board/uXjVEbl3LCk=/)  

---

## Desafio 5 — Isomorfismo

**G:** V = {1, 2, 3, 4}; E = {(1,2), (2,3), (3,4), (4,1)}  
**H:** V = {a, b, c, d}; E = {(a,c), (c,b), (b,d), (d,a)}

### 1. Ordem e tamanho

| Grafo | Ordem \|V\| | Tamanho \|E\| |
| :---: | :---: | :---: |
| G | 4 | 4 |
| H | 4 | 4 |

### 2. Graus e sequência de graus

| Vértice em G | Grau | Vértice em H | Grau |
| :---: | :---: | :---: | :---: |
| 1 (vizinhos 2 e 4) | 2 | a (vizinhos c e d) | 2 |
| 2 (vizinhos 1 e 3) | 2 | b (vizinhos c e d) | 2 |
| 3 (vizinhos 2 e 4) | 2 | c (vizinhos a e b) | 2 |
| 4 (vizinhos 1 e 3) | 2 | d (vizinhos a e b) | 2 |

Sequência de graus de G: **(2, 2, 2, 2)**  
Sequência de graus de H: **(2, 2, 2, 2)**

### 3. Correspondência entre os vértices

| Vértice em G | Correspondente em H |
| :---: | :---: |
| 1 | a |
| 2 | c |
| 3 | b |
| 4 | d |

A correspondência foi obtida percorrendo o ciclo de cada grafo: 1 → 2 → 3 → 4 → 1 em G e a → c → b → d → a em H.

### 4. Verificação aresta por aresta

Seja f a função definida na tabela acima. Para cada aresta (u, v) de G, verifica-se se (f(u), f(v)) pertence a E(H):

| Aresta em G | Imagem por f | Pertence a E(H)? |
| :---: | :---: | :---: |
| (1,2) | (a,c) | Sim |
| (2,3) | (c,b) | Sim |
| (3,4) | (b,d) | Sim |
| (4,1) | (d,a) | Sim |

As quatro arestas de G são levadas em quatro arestas distintas de H. Como H possui exatamente quatro arestas, nenhuma aresta de H ficou sem correspondente; portanto, f preserva a adjacência e a não adjacência (u e v são adjacentes em G se, e somente se, f(u) e f(v) são adjacentes em H).

### 5. Conclusão e justificativa

**Os grafos G e H são isomorfos.**

*Justificativa:* G e H possuem a mesma ordem (4), o mesmo tamanho (4) e a mesma sequência de graus (2, 2, 2, 2). Além disso, a função f: V(G) → V(H), com f(1) = a, f(2) = c, f(3) = b e f(4) = d, é uma bijeção que preserva todas as adjacências, conforme verificado aresta por aresta. Ambos os grafos são o ciclo de quatro vértices (C₄); a diferença está apenas nos rótulos e na forma do desenho (quadrado em G e losango em H), o que não altera a estrutura.

### Reflexão

**Ter a mesma sequência de graus é suficiente para garantir isomorfismo?**

Não. A igualdade da sequência de graus é uma condição necessária, mas não suficiente. Dois grafos isomorfos sempre possuem a mesma sequência de graus, porém a recíproca é falsa. Contraexemplo: o ciclo C₆ (um único ciclo com seis vértices) e a união disjunta de dois triângulos possuem, ambos, seis vértices, seis arestas e sequência de graus (2, 2, 2, 2, 2, 2). Contudo, C₆ é conexo e a união de dois triângulos não é; logo, não existe bijeção que preserve as adjacências, e os grafos não são isomorfos. Por isso é necessário exibir a correspondência entre os vértices e verificar as arestas, e não apenas comparar os graus.

---

## Desafio 7 — Sequência de graus

**Sequência solicitada (ordem não decrescente):** (1, 1, 2, 3, 3, 4, 4, 6)  
**Condição:** grafo simples (sem laços e sem arestas paralelas) com oito vértices.

### Planejamento

A soma da sequência é 1 + 1 + 2 + 3 + 3 + 4 + 4 + 6 = 24, valor par, de modo que o grafo deve ter 24 / 2 = 12 arestas. O vértice de maior grau (A, grau 6) foi ligado a seis dos outros sete vértices; os demais vértices foram então completados com as arestas restantes, sem repetir pares e sem usar laços.

### Construção progressiva das arestas

| Passo | Arestas adicionadas |
| :---: | :--- |
| 1 | (A,B), (A,C), (A,D), (A,E), (A,F), (A,G) — o vértice A atinge o grau 6 |
| 2 | (B,C), (B,D), (B,E) — o vértice B atinge o grau 4 |
| 3 | (C,D), (C,H) — o vértice C atinge o grau 4 |
| 4 | (E,F) — os vértices E e F atingem os graus 3 e 2 |

### Vértices e graus obtidos

| Vértice | Grau obtido | Vizinhos |
| :---: | :---: | :--- |
| A | 6 | B, C, D, E, F, G |
| B | 4 | A, C, D, E |
| C | 4 | A, B, D, H |
| D | 3 | A, B, C |
| E | 3 | A, B, F |
| F | 2 | A, E |
| G | 1 | A |
| H | 1 | C |

### Conjunto de arestas

**E = {(A,B), (A,C), (A,D), (A,E), (A,F), (A,G), (B,C), (B,D), (B,E), (C,D), (C,H), (E,F)}**

Não há laços (nenhum par da forma (X,X)) e nenhum par se repete; portanto, o grafo é simples.

### Conferência

- **Sequência obtida (ordem não decrescente):** (1, 1, 2, 3, 3, 4, 4, 6)  
  G(1), H(1), F(2), D(3), E(3), B(4), C(4), A(6).
- **Soma dos graus:** 24  **Número de arestas:** 12
- **Verificação:** soma dos graus = 2 × número de arestas → 24 = 2 × 12 → **Sim.**

A sequência obtida coincide com a solicitada. A igualdade entre a soma dos graus e o dobro do número de arestas corresponde ao Lema do Aperto de Mãos: cada aresta contribui com uma unidade ao grau de cada uma de suas duas extremidades.

---

## Como reproduzir no Graph Online

Os grafos foram construídos no Miro (link no cabeçalho). Para refazê-los no Graph Online (https://graphonline.ru), basta criar os vértices e ligar os pares abaixo:

- **G:** 1–2, 2–3, 3–4, 4–1  
- **H:** a–c, c–b, b–d, d–a  
- **Desafio 7:** A–B, A–C, A–D, A–E, A–F, A–G, B–C, B–D, B–E, C–D, C–H, E–F

## Referência

GOMES, Paulo César Rodacki. **Grafos: conceitos fundamentais, algoritmos e aplicações**. Blumenau: Editora IFC, 2022. Capítulo 1.
