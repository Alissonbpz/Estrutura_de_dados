valores = []

while True:

    print("\nOpções:")
    print("\n[0] - Listar valores"
          "\n[1] - Buscar por índice"
          "\n[2] - Buscar por valor"
          "\n[3] - Inserir"
          "\n[4] - Remover"
          "\n[5] - Parar")

    opcao = int(input("\nDigite a opção desejada: "))

    if opcao == 5:
        break

    elif opcao == 0:
        print("\nValores:", valores)

    elif opcao == 1:
        i = int(input("\nDigite o índice do valor que deseja buscar: "))

        if 0 <= i < len(valores):
            print("\nValor:", valores[i])
        else:
            print("\nÍndice inválido.")

    elif opcao == 2:
        v = input("\nDigite o valor que deseja buscar: ")

        for i in range(len(valores)):
            if valores[i] == v:
                print("\nValor encontrado no índice:", i)
                break
        else:
            print("\nValor não encontrado.")

    elif opcao == 3:
        v = input("\nDigite o valor que deseja inserir: ")

        valores = valores + [v]

        print("\nValor inserido com sucesso.")

    elif opcao == 4:
        v = input("\nDigite o valor que deseja remover: ")

        nova = []

        for i in range(len(valores)):
            if valores[i] != v:
                nova = nova + [valores[i]]

        if len(nova) == len(valores):
            print("\nValor não encontrado.")
        else:
            valores = nova
            print("\nValor removido com sucesso.")

    else:
        print("\nOpção inválida.")