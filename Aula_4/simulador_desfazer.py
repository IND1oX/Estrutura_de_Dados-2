# Simulador de Desfazer
# Estrutura: Pilha (LIFO)

pilha = []
contador = 1


while True:

    print("\n===================================")
    print("        SIMULADOR DE DESFAZER")
    print("===================================")
    print("1 - Digitar")
    print("2 - Apagar")
    print("3 - Substituir")
    print("4 - Desfazer última ação (Ctrl+Z)")
    print("5 - Mostrar histórico de ações")
    print("6 - Mostrar quantidade de ações")
    print("0 - Sair")
    print("-----------------------------------")

    opcao = input("Escolha uma opção: ")

    if opcao in ("1", "2", "3"):

        if opcao == "1":
            tipo = "Digitar"
        elif opcao == "2":
            tipo = "Apagar"
        else:
            tipo = "Substituir"

        conteudo = input("Descreva o conteúdo da ação: ")

        acao = {
            "numero": contador,
            "tipo": tipo,
            "conteudo": conteudo
        }

        pilha.append(acao)

        print("\nAção registrada no topo da pilha.")

        contador += 1

    elif opcao == "4":

        if len(pilha) > 0:

            acao = pilha.pop()

            print("\n===== DESFAZER =====")
            print("Ação removida:", acao["tipo"])
            print("Conteúdo:", acao["conteudo"])
            print("Ação desfeita com sucesso.")

        else:

            print("Não existem ações para desfazer.")

    elif opcao == "5":

        if len(pilha) > 0:

            print("\n===== HISTÓRICO (TOPO -> BASE) =====")

            posicao = 1

            for acao in reversed(pilha):

                print(
                    str(posicao) + "º -",
                    acao["tipo"],
                    "|",
                    acao["conteudo"]
                )

                posicao += 1

        else:

            print("A pilha está vazia.")

    elif opcao == "6":

        print(
            "Quantidade de ações na pilha:",
            len(pilha)
        )

    elif opcao == "0":

        print("Sistema encerrado.")
        break

    else:

        print("Opção inválida.")
