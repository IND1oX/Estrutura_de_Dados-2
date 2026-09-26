🌳 **Unique Trees: AVL Upgrade Edition**

Projeto desenvolvido em grupo para a disciplina de Estruturas de Dados II, do curso de Ciência da Computação.

O Unique Trees: AVL Upgrade Edition é um jogo educativo interativo e gráfico desenvolvido em Python utilizando a biblioteca Pygame. O objetivo do projeto é ensinar de forma prática o funcionamento e as operações de balanceamento das Árvores AVL, permitindo que o estudante participe ativamente na manutenção das propriedades da árvore e na aplicação de rotações simples e duplas.

🎯 **Objetivo**

Transformar a aprendizagem teórica das Árvores AVL em uma atividade interativa. O jogador assume o papel de um jardineiro que deve plantar sementes numeradas mantendo a árvore equilibrada dentro dos limites de altura do canteiro (canopy budget), realizando a Poda Direcionada (Rotação AVL) sempre que o Fator de Balanceamento (FB) atingir um estado crítico.

📚 **Contexto do Projeto e Modelo Reutilizado**

O projeto tomou como base o jogo minimalista "Unique Trees" (Playcebo, itch.io, 2024).

Limitação do Modelo Original: O jogo original tratava a árvore de forma puramente estética e combinatória, sem exigir regras de inserção ordenada, restrições de altura, penalidades de desempenho ou rotações algorítmicas.

A Proposta de Upgrade: O grupo implementou a mecânica de Árvore AVL, onde o crescimento respeita a propriedade de Árvore Binária de Busca (BST) e exige ações ativas do jogador para balancear o Fator de Balanceamento (FB∈{−1,0,1}) através de rotações.

⚙️ **Mapeamento de Conceitos de ED II em Mecânicas**

| Conceito Teórico de ED II | Elemento / Mecânica Correspondente no Jogo |
| --- | --- |
| Nó / Chave | Broto plantado no canteiro com uma semente numerada definindo sua posição relativa. |
| Altura da Árvore (h) | Extensão vertical do canteiro (canopy budget); limita a altura máxima permitida. |
| Fator de Balanceamento (FB) | Indicador de Seiva e cor sobre cada nó (FB∈{−1,0,1} = Verde/Estável; FB=±2 = Vermelho/Piscante). |
| Operação de Correção | Poda Direcionada: Ação do jogador ao clicar com o botão direito sobre um nó crítico para disparar a Rotação AVL. |

🕹️ **Mecânica do Jogo e Core Loop**

- Plantar Sementes: O jogador clica com o Botão Esquerdo para plantar a próxima semente numerada no canteiro, seguindo as regras de uma Árvore Binária de Busca.
- Monitorar a Seiva (FB): O jogo recalcula e exibe o FB em tempo real acima de cada nó.
- Poda Direcionada (Rotação AVL): Quando um nó atinge FB=±2, o jogador deve clicar com o Botão Direito sobre ele para disparar a rotação necessária (LL, RR, LR ou RL).
- Tooltips Educacionais: Ao passar o mouse sobre um nó crítico, o jogo exibe qual rotação exata é necessária para rebalanceá-lo.

⚠️ **Condições de Vitória e Derrota**

🏆 Condição de Vitória: Plantar todas as sementes da fase mantendo todos os nós balanceados com FB∈{−1,0,1} e dentro do limite de altura. O jogador recebe uma classificação de 1 a 3 estrelas (⭐) com base na eficiência das rotações.

❌ Condição de Derrota (Degeneração): Se o jogador tentar plantar uma nova semente mantendo um nó em estado crítico (FB=±2), o ramo murcha e a árvore colapsa para um caule reto, representando a degeneração da estrutura para uma lista encadeada e a perda da eficiência O(log n).

🐍 **Tecnologias Utilizadas**

- Python 3
- Pygame (Interface gráfica, manipulação de eventos e efeitos visuais)
- Pygame Mixer (Sintetização interna de áudio e efeitos sonoros)
- Math & Random (Cálculo de vetores para partículas e animações de interpolação)

▶️ **Como Executar**

Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina e instale a biblioteca Pygame:

```bash
pip install pygame
```

Executando o Jogo

Navegue até a pasta do projeto e execute o arquivo principal:

```bash
python arvore_avancada_imp.py
```

🎮 **Controles no Teclado/Mouse**

- Botão Esquerdo do Mouse: Planta a próxima semente.
- Botão Direito do Mouse: Realiza a rotação AVL no nó crítico selecionado.
- Tecla R: Reinicia o nível atual.
- Tecla N: Avança para a próxima fase / nível.
- Tecla P: Volta para a fase anterior.

📁 **Arquivos do Projeto**

```
📦 Extra_Arvores_Avancadas
 ├── 📄 GDD_Arvores_AVL_UniqueTrees.pdf                # GDD preenchido pelo grupo
 ├── 📄 aula_arvores_ed2_260911_191439.pdf             # Plano de aula da professora
 ├── 📄 Guia_de_Atividade_Prática...docx               # Template do guia de atividade
 ├── 📄 arvore_avancada_imp.py                         # Código-fonte principal do jogo
 └── 📄 README.md                                      # Documentação do projeto
```

👥 **Integrantes do Grupo**

- Gustavo Alves
- Arthur Bernardo
- Kelly da Silva
- Brenda Ribeiro

Disciplina: Estruturas de Dados II
Curso: Ciência da Computação
Turma: N1 / Ciência da Computação
Data: 25/09/2026
