# =====================================================================
# 1. DEFINIÇÃO DO NÓ DUPLO (NODE DUPLO)
# =====================================================================
class NodeDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None


# =====================================================================
# 2. DEFINIÇÃO DA LISTA DUPLAMENTE ENCADEADA (ESQUELETO)
# =====================================================================
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

    def imprimir_frente(self):
        atual = self.cabeca

        while atual is not None:
            print(atual.dado)
            atual=atual.proximo

    def imprimir_tras(self):
        atual = self.cauda
        
        while atual is not None:
            print(atual.dado)
            atual=atual.anterior