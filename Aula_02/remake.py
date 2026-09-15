"""
Implementação de uma Lista Sequencial Estática em Python sem utilizar os recursos de bibliotecas

Operações:

    buscar_por_indice
    buscar_por_valor
    inserir
    remover
"""

lista = []

while True:
    print("Lista atual:", lista)
    print("Escolha uma operação:")
    print("1. Buscar por índice")
    print("2. Buscar por valor")
    print("3. Inserir")
    print("4. Remover")
    print("5. Sair")

    opcao = int(input("Digite o número da operação desejada: "))

    if opcao == 1:
        indice = int(input("Digite o indice desejado: "))
        if 0 <= indice < len(lista):
            print("Valor no indice ", indice, " da lista e ", lista[indice])
        else:
            print("A lista nao possui este indice.")
    elif opcao == 2:
        encontrado = False
        valor = int(input("Digite o valor desejado: "))
        for i in range(len(lista)):
            if valor == lista[i]:
                encontrado = True
                print("Valor ",valor, "esta no indice ", i , "da lista ")
        if not encontrado:
            print("Este valor nao esta na lista.")
    elif opcao == 3:
        inserir = int(input("Digite o valor que deseja inserir: "))
        b =[inserir]
        lista = lista + b
    elif opcao == 4:
        encontrado = False
        valor = int(input("Digite o valor que deseja remover da lista: "))

        for i in range(len(lista)):
            if valor == lista[i]:
                encontrado = True
                lista[i] = None
                print("Valor retirado da lista.")
        if not encontrado:
            print("Este valor nao esta na lista.")
    elif opcao == 5:
        break