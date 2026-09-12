# Sistema de Triagem Hospitalar
# Estrutura: Fila com Prioridade

from collections import deque


fila_emergencia = deque()
fila_preferencial = deque()
fila_normal = deque()


while True:

    print("\n===================================")
    print("       TRIAGEM HOSPITALAR")
    print("===================================")
    print("1 - Cadastrar paciente")
    print("2 - Atender paciente")
    print("3 - Mostrar fila")
    print("4 - Mostrar quantidade de pacientes")
    print("0 - Sair")
    print("-----------------------------------")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome do paciente: ")

        print("\nEscolha a prioridade:")
        print("1 - Emergência")
        print("2 - Preferencial")
        print("3 - Normal")

        prioridade = input("Prioridade: ")

        paciente = {
            "nome": nome
        }

        if prioridade == "1":

            paciente["prioridade"] = "Emergência"

            fila_emergencia.append(paciente)

            print(
                "Paciente cadastrado como emergência."
            )

        elif prioridade == "2":

            paciente["prioridade"] = "Preferencial"

            fila_preferencial.append(paciente)

            print(
                "Paciente cadastrado como preferencial."
            )

        elif prioridade == "3":

            paciente["prioridade"] = "Normal"

            fila_normal.append(paciente)

            print(
                "Paciente cadastrado como atendimento normal."
            )

        else:

            print("Prioridade inválida.")

    elif opcao == "2":

        if len(fila_emergencia) > 0:

            paciente = fila_emergencia.popleft()

        elif len(fila_preferencial) > 0:

            paciente = fila_preferencial.popleft()

        elif len(fila_normal) > 0:

            paciente = fila_normal.popleft()

        else:

            print("Não existem pacientes aguardando.")
            continue

        print("\n===== ATENDIMENTO =====")
        print("Paciente:", paciente["nome"])
        print("Prioridade:", paciente["prioridade"])
        print("Paciente encaminhado para atendimento.")

    elif opcao == "3":

        print("\n===== FILA DE ATENDIMENTO =====")

        posicao = 1

        for paciente in fila_emergencia:

            print(
                str(posicao) + "º -",
                paciente["nome"],
                "|",
                paciente["prioridade"]
            )

            posicao += 1

        for paciente in fila_preferencial:

            print(
                str(posicao) + "º -",
                paciente["nome"],
                "|",
                paciente["prioridade"]
            )

            posicao += 1

        for paciente in fila_normal:

            print(
                str(posicao) + "º -",
                paciente["nome"],
                "|",
                paciente["prioridade"]
            )

            posicao += 1

        if posicao == 1:

            print("A fila está vazia.")

    elif opcao == "4":

        total = (
            len(fila_emergencia)
            + len(fila_preferencial)
            + len(fila_normal)
        )

        print(
            "\nTotal de pacientes aguardando:",
            total
        )

        print(
            "Emergência:",
            len(fila_emergencia)
        )

        print(
            "Preferencial:",
            len(fila_preferencial)
        )

        print(
            "Normal:",
            len(fila_normal)
        )

    elif opcao == "0":

        print("Sistema encerrado.")
        break

    else:

        print("Opção inválida.")
