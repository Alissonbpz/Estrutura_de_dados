"""Tema: Modelagem e Gerenciamento do Sistema de Trem de Carga
1. Objetivo

Compreender e aplicar na prática os conceitos de alocação dinâmica de memória e ponteiros/referências em Python.
2. Descrição do Cenário

Uma empresa de logística ferroviária precisa de um módulo para gerenciar a composição de seus trens de carga. Cada vagão é um elemento independente na memória (um nó) que armazena suas próprias informações e aponta para o vagão imediatamente subsequente.

Você deverá implementar a classe Node para representar cada vagão e desenvolver funções específicas para percorrer, alterar, remover e reordenar os elementos da corrente.
3. Requisitos de Implementação
3.1. Estrutura do Nó (Classe Node)

Defina a classe Node (representando um vagão). Cada instância deve possuir três atributos inicializados no método construtor __init__:

    nome (string): Identificador do vagão (exemplo: "Locomotiva").

    peso (float): Peso do vagão em toneladas.

    proximo (Node): Referência para o próximo nó da corrente (inicialmente None).

3.2. Montagem Inicial da Composição

Instancie e encadeie manualmente a seguinte sequência inicial de vagões:

    Locomotiva — Peso: 80.0 t

    Vagão Carga — Peso: 50.0 t

    Vagão Passageiros — Peso: 30.0 t

    Vagão Cauda — Peso: 10.0 t

3.3. Função de Relatório e Varredura (relatorio_trem)

Implemente a função relatorio_trem(primeiro_no) que recebe o nó inicial (cabeça da lista) e percorre a estrutura utilizando uma estrutura de repetição while.

A função deve exibir:

    A representação visual da sequência de vagões no formato:

    [ Locomotiva (80.0t) ] -> [ Vagão Carga (50.0t) ] -> ... -> FIM

    A quantidade total de vagões conectados.

    O peso total acumulado da composição (soma dos pesos de todos os vagões).

3.4. Operação de Inserção Intermediária

Sem recriar a estrutura existente, insira um novo nó chamado "Vagão Restaurante" (peso: 25.0 t) entre o "Vagão Carga" e o "Vagão Passageiros".

Atenção: A inserção deve ser feita exclusivamente através do ajuste das referências do atributo proximo.
3.5. Operação de Remoção (desengatar_vagao)

Implemente a função desengatar_vagao(primeiro_no, nome_alvo) que recebe a cabeça do trem e o nome de um vagão a ser removido.

    A função deve localizar o vagão, ajustar os ponteiros dos nós adjacentes para removê-lo da corrente e redefinir o atributo proximo do nó removido para None.

    A função deve retornar a nova cabeça do trem (para tratar corretamente os casos em que o primeiro nó é o removido).

    Teste da função: Remova o nó "Vagão Carga" e imprima o relatório atualizado.

3.6. Desafio Avançado: Inversão de Ponteiros (inverter_trem)

Implemente a função inverter_trem(primeiro_no) que inverta totalmente o sentido de navegação do trem alterando apenas as referências proximo armazenadas nos nós.

    Restrição: É proibido criar novos objetos Node ou utilizar listas auxiliares para a conversão.

    A função deve retornar a nova cabeça da composição (o nó que anteriormente representava a cauda).

4. Restrições Técnicas Obrigatórias

    É estritamente proibido utilizar estruturas de dados nativas do Python para armazenar a sequência dos vagões, tais como list, tuple, dict ou set.

    Toda a navegação, inserção e remoção deve ser feita manipulação direta de referências de objetos (no.proximo).
"""
class Node:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.proximo = None

no1 = Node("locomotiva", 80.0)
no2 = Node("Vagao carga", 50.0)
no3 = Node("Vagao passageiros", 30.0)
no4 = Node("vagao cauda", 10.0)

no1.proximo = no2
no2.proximo = no3
no3.proximo = no4

cabeca = no1

def relatorio_trem(primeiro_no):
    atual = primeiro_no
    vagoes = ""
    quantidade = 0
    peso_total = 0.0

    while atual is not None:
        vagoes+= f"[ {atual.nome} ({atual.peso}t) ] -> "
        quantidade += 1
        peso_total += atual.peso
        atual = atual.proximo

    vagoes+="FIM"
    print(vagoes)
    print(f"Quantidade de vagões: {quantidade}")
    print(f"Peso total da composição: {peso_total}t")
    print("-" * 60)
    
relatorio_trem(cabeca)

no5 = Node("Vagao restaurante", 25.0)

cabeca.proximo = no2
no2.proximo = no3
no3.proximo = no5
no5.proximo = no4

relatorio_trem(cabeca)

def desengatar_vagao(primeiro_no, nome_alvo):
    anterior = None
    atual = primeiro_no

    while atual is not None:
        if atual.nome == nome_alvo:
            if anterior == None:
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

cabeca = desengatar_vagao(cabeca, "Vagao carga")

relatorio_trem(cabeca)

def inverter_trem(primeiro_no):
    atual = primeiro_no
    anterior = None

    while atual is not None:
        proximo = atual.proximo
        atual.proximo = anterior
        anterior = atual
        atual = proximo

    return anterior

cabeca = inverter_trem(cabeca)

relatorio_trem(cabeca)


