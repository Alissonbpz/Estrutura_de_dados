from os import dup


class NodeDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def esta_vazia(self) -> bool:
        return self.cabeca is None

    def inserir_inicio(self, valor):
        novo_no = NodeDuplo(valor)
        if self.esta_vazia():
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca= novo_no

    def inserir_fim(self, valor):
        novo_no = NodeDuplo(valor)
        if self.esta_vazia():
            self.cabeca = novo_no
            self.cauda=novo_no
        else:
            novo_no.anterior = self.cauda
            self.cauda.proximo = novo_no
            self.cauda = novo_no

# =====================================================================
#           """Problema da prova: remover_duplicados()"""
# =====================================================================
    def remover_duplicados(self):
        atual = self.cabeca
        
        if atual == None:
            print("Lista vazia sem nós duplicados.")
            return
    
        while atual is not None:
            duplicado = atual.proximo

            while duplicado is not None:
                proximo_valor = duplicado.proximo
                if duplicado.dado == atual.dado:
                    if duplicado.anterior is not None:
                        duplicado.anterior.proximo = duplicado.proximo
                    if duplicado.proximo is not None:
                        duplicado.proximo.anterior = duplicado.anterior
                    if duplicado == self.cauda:
                        self.cauda = duplicado.anterior
                duplicado = proximo_valor
            atual = atual.proximo
# =====================================================================             

# =====================================================================       

    def imprimir_frente(self):
            atual = self.cabeca
            while atual is not None:
                print(atual.dado,",")
                atual = atual.proximo
    
    def imprimir_tras(self):
        atual = self.cauda
        print("\nDe trás pra frente: \n")
        while atual is not None:
            print(atual.dado,", ")
            atual = atual.anterior

lista = ListaDuplamenteEncadeada()

print("\n--- Teste: Lista inicial (10, 20, 10, 30, 20, 40) ---")

lista.inserir_inicio(10)
lista.inserir_fim(20)
lista.inserir_fim(10)
lista.inserir_fim(30)
lista.inserir_fim(20)
lista.inserir_fim(40)
lista.imprimir_frente()
lista.imprimir_tras()

print("\n--- Teste: Removendo valores duplicados(10, 20, 30, 40) ---")

lista.remover_duplicados()
lista.imprimir_frente()
lista.imprimir_tras()
