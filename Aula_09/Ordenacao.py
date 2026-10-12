def bubble_sort(v):
    comparacoes = 0
    trocas = 0
    n = len(v)

    for i in range(n - 1):
        trocou = False  

        for j in range(n - 1 - i):
            comparacoes += 1  
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                trocas += 1
                trocou = True

        if not trocou:
            break

    return comparacoes, trocas


def selection_sort(v):
    comparacoes = 0
    trocas = 0
    n = len(v)

    for i in range(n - 1):
        m = i  

        for j in range(i + 1, n):
            comparacoes += 1  
            if v[j] < v[m]:
                m = j

        if m != i:
            v[i], v[m] = v[m], v[i]
            trocas += 1

    return comparacoes, trocas


def insertion_sort(v):
    comparacoes = 0
    deslocamentos = 0
    n = len(v)

    for i in range(1, n):
        chave = v[i]  
        j = i - 1

        while j >= 0:
            comparacoes += 1 
            if v[j] > chave:
                v[j + 1] = v[j]  
                deslocamentos += 1
                j -= 1
            else:
                break

        v[j + 1] = chave  

    return comparacoes, deslocamentos

if __name__ == "__main__":
    aleatorio = [64, 25, 12, 22, 11, 90, 42]
    quase = [10, 20, 30, 50, 40, 60, 70]
    invertido = [70, 60, 50, 40, 30, 20, 10]

    vetores = [
        ("Aleatório", aleatorio),
        ("Quase ordenado", quase),
        ("Invertido", invertido),
    ]

    algoritmos = [
        ("Bubble", bubble_sort),
        ("Selection", selection_sort),
        ("Insertion", insertion_sort),
    ]

    print(f"{'Vetor':<16}{'Algoritmo':<12}{'Comparações':<14}{'Trocas/Desloc.':<16}{'Ordenou?'}")
    print("-" * 66)

    for nome_vetor, original in vetores:
        for nome_alg, funcao in algoritmos:
            v = list(original)  
            comp, mov = funcao(v)
            ok = "sim" if v == sorted(original) else "NÃO"
            print(f"{nome_vetor:<16}{nome_alg:<12}{comp:<14}{mov:<16}{ok}")
        print()
