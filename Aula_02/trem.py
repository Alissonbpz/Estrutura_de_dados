class Node:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.proximo = None


no1 = Node("Locomotiva", 80.0)
no2 = Node("Vagão Carga", 50.0)
no3 = Node("Vagão Passageiros", 30.0)
no4 = Node("Vagão Cauda", 10.0)

no1.proximo = no2
no2.proximo = no3
no3.proximo = no4

cabeca = no1


def relatorio_trem(primeiro_no):
    atual = primeiro_no
    representacao = ""
    quantidade = 0
    peso_total = 0.0

    while atual is not None:
        representacao += f"[ {atual.nome} ({atual.peso}t) ] -> "
        quantidade += 1
        peso_total += atual.peso
        atual = atual.proximo

    representacao += "FIM"

    print(representacao)
    print(f"Quantidade de vagões: {quantidade}")
    print(f"Peso total da composição: {peso_total}t")
    print("-" * 60)


print("=== Composição inicial ===")
relatorio_trem(cabeca)


vagao_restaurante = Node("Vagão Restaurante", 25.0)

atual = cabeca
while atual is not None:
    if atual.nome == "Vagão Carga":
        vagao_restaurante.proximo = atual.proximo
        atual.proximo = vagao_restaurante
        break
    atual = atual.proximo

print("=== Após inserir Vagão Restaurante ===")
relatorio_trem(cabeca)


def desengatar_vagao(primeiro_no, nome_alvo):
    anterior = None
    atual = primeiro_no

    while atual is not None:
        if atual.nome == nome_alvo:
            if anterior is None:
                nova_cabeca = atual.proximo
                atual.proximo = None
                return nova_cabeca
            else:
                anterior.proximo = atual.proximo
                atual.proximo = None
                return primeiro_no
        anterior = atual
        atual = atual.proximo

    return primeiro_no


cabeca = desengatar_vagao(cabeca, "Vagão Carga")

print("=== Após remover Vagão Carga ===")
relatorio_trem(cabeca)


def inverter_trem(primeiro_no):
    anterior = None
    atual = primeiro_no

    while atual is not None:
        proximo_temp = atual.proximo
        atual.proximo = anterior
        anterior = atual
        atual = proximo_temp

    return anterior


cabeca = inverter_trem(cabeca)

print("=== Após inverter o trem ===")
relatorio_trem(cabeca)
