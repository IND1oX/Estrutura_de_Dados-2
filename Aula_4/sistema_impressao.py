# Sistema de Impressão
# Estrutura: Fila (FIFO)

from collections import deque


fila = deque()
contador = 1


while True:

    print("\n===================================")
    print("        SISTEMA DE IMPRESSÃO")
    print("===================================")
    print("1 - Adicionar documento")
    print("2 - Imprimir próximo documento")
    print("3 - Mostrar fila")
    print("4 - Mostrar quantidade de documentos")
    print("0 - Sair")
    print("-----------------------------------")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome do documento: ")

        try:

            paginas = int(input("Quantidade de páginas: "))

            if paginas <= 0:
                print("A quantidade de páginas deve ser maior que zero.")
                continue

        except ValueError:

            print("Digite um número válido.")
            continue

        documento = {
            "numero": contador,
            "nome": nome,
            "paginas": paginas
        }

        fila.append(documento)

        print("\nDocumento adicionado à fila.")

        contador += 1

    elif opcao == "2":

        if len(fila) > 0:

            documento = fila.popleft()

            print("\n===== IMPRESSÃO =====")
            print("Documento:", documento["nome"])
            print("Páginas:", documento["paginas"])
            print("Impressão concluída.")

        else:

            print("Não existem documentos aguardando.")

    elif opcao == "3":

        if len(fila) > 0:

            print("\n===== FILA DE IMPRESSÃO =====")

            posicao = 1

            for documento in fila:

                print(
                    str(posicao) + "º -",
                    documento["nome"],
                    "|",
                    documento["paginas"],
                    "páginas"
                )

                posicao += 1

        else:

            print("A fila está vazia.")

    elif opcao == "4":

        print(
            "Quantidade de documentos aguardando:",
            len(fila)
        )

    elif opcao == "0":

        print("Sistema encerrado.")
        break

    else:

        print("Opção inválida.")
