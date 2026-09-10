# =====================================================================
# DEFINIÇÃO DOS NÓS
# =====================================================================
class NodeSimples:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class NodeDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None


# =====================================================================
# 1. VETOR ESTÁTICO
# =====================================================================
class VetorEstatico:
    def __init__(self, capacidade=10):
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.tamanho = 0

    def inserir(self, valor) -> bool:
        if self.tamanho >= self.capacidade:
            return False
        self.dados[self.tamanho] = valor
        self.tamanho += 1
        return True

    def remover_impares(self):
        """Remove ímpares deslocando os elementos restantes à esquerda."""
        if self.tamanho == 0:
            return
        else:
            novo_tamanho = 0
            for i in range(self.tamanho):
                if self.dados[i] % 2 == 0:
                    self.dados[novo_tamanho] = self.dados[i]
                    novo_tamanho += 1
            self.tamanho = novo_tamanho

    def exportar_para_lista_simples(self) -> 'ListaSimples':
        """Cria e retorna uma ListaSimples com os dados válidos do vetor."""
        lista_simples = ListaSimples()
        for i in range(self.tamanho):
            lista_simples.append(self.dados[i])
        return lista_simples

    def imprimir(self):
        print("Vetor:", [self.dados[i] for i in range(self.tamanho)])


# =====================================================================
# 2. LISTA SIMPLESMENTE ENCADEADA
# =====================================================================
class ListaSimples:
    def __init__(self):
        self.cabeca = None

    def append(self, valor):
        self.inserir_fim(valor)

    def inserir_fim(self, valor):
        """Insere um novo nó no final da lista simples."""
        novo = NodeSimples(valor)
        if self.cabeca is None:
            self.cabeca = novo
            return
        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo

    def inverter(self):
        """Inverte a ordem dos nós in-place (reorientando apenas ponteiros .proximo)."""
        anterior = None
        atual = self.cabeca
        while atual is not None:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
        self.cabeca = anterior

    def converter_para_dupla(self) -> 'ListaDupla':
        """Cria e retorna uma ListaDupla com os elementos desta lista."""
        lista_dupla = ListaDupla()
        atual = self.cabeca
        while atual is not None:
            lista_dupla.inserir_fim(atual.dado)
            atual = atual.proximo
        return lista_dupla

    def imprimir(self):
        itens = []
        atual = self.cabeca
        while atual is not None:
            itens.append(str(atual.dado))
            atual = atual.proximo
        conteudo = " -> ".join(itens) + " -> None" if itens else "Vazia"
        print(f"Lista Simples: {conteudo}")


# =====================================================================
# 3. LISTA DUPLAMENTE ENCADEADA
# =====================================================================
class ListaDupla:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def inserir_fim(self, valor):
        """Insere no fim amarrando .anterior, .proximo e atualizando self.cauda."""
        novo = NodeDuplo(valor)
        if self.cabeca is None:
            self.cabeca = novo
            self.cauda = novo
        else:
            novo.anterior = self.cauda
            self.cauda.proximo = novo
            self.cauda = novo
        self.tamanho += 1

    def split_metade(self):
        """
        Divide a lista ao meio.
        Retorna duas novas instâncias de ListaDupla: (metade1, metade2).
        """
        metade1 = ListaDupla()
        metade2 = ListaDupla()
        primeira_parte = self.tamanho // 2
        atual = self.cabeca
        i = 0
        while atual is not None:
            if i < primeira_parte:
                metade1.inserir_fim(atual.dado)
            else:
                metade2.inserir_fim(atual.dado)
            atual = atual.proximo
            i += 1
        return metade1, metade2

    def imprimir_frente(self):
        itens = []
        atual = self.cabeca
        while atual is not None:
            itens.append(str(atual.dado))
            atual = atual.proximo
        conteudo = " <-> ".join(itens) + " -> None" if itens else "Vazia"
        print(f"Dupla Frente: {conteudo}")

    def imprimir_tras(self):
        itens = []
        atual = self.cauda
        while atual is not None:
            itens.append(str(atual.dado))
            atual = atual.anterior
        conteudo = " <-> ".join(itens) + " -> None" if itens else "Vazia"
        print(f"Dupla Trás:   {conteudo}")


# =====================================================================
# 4. LISTA CIRCULAR (DUPLA)
# =====================================================================
class ListaCircular:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    @classmethod
    def criar_a_partir_de_dupla(cls, lista_dupla: ListaDupla) -> 'ListaCircular':
        """Recebe uma ListaDupla e fecha o anel (cauda <-> cabeca)."""
        circular = cls()
        circular.cabeca = lista_dupla.cabeca
        circular.cauda = lista_dupla.cauda
        circular.tamanho = lista_dupla.tamanho
        if circular.cabeca is not None:
            circular.cauda.proximo = circular.cabeca
            circular.cabeca.anterior = circular.cauda
        return circular

    def girar_e_eliminar(self, passos: int) -> int:
        """
        A partir do nó atual, avança (passos - 1) vezes pelo ponteiro .proximo,
        remove o nó onde parou e religa os vizinhos no anel.
        O próximo ciclo recomeça a partir do nó seguinte ao removido.
        Repete até restar apenas 1 nó e retorna o seu dado.
        """
        if self.tamanho == 0:
            return None

        atual = self.cabeca
        while self.tamanho > 1:
            for _ in range(passos - 1):
                atual = atual.proximo

            anterior_no = atual.anterior
            proximo_no = atual.proximo
            anterior_no.proximo = proximo_no
            proximo_no.anterior = anterior_no

            if atual is self.cabeca:
                self.cabeca = proximo_no
            if atual is self.cauda:
                self.cauda = anterior_no

            self.tamanho -= 1
            atual = proximo_no

        return atual.dado

    def imprimir_uma_volta(self):
        if self.cabeca is None:
            print("Circular (1 volta): Vazia")
            return
        itens = []
        atual = self.cabeca
        for _ in range(self.tamanho):
            itens.append(str(atual.dado))
            atual = atual.proximo
        print("Circular (1 volta): " + " -> ".join(itens) + " -> [volta ao início]")


# =====================================================================
# EXECUÇÃO DE TESTE
# =====================================================================
if __name__ == "__main__":
    print("=== ETAPA 1: VETOR ESTÁTICO ===")
    v = VetorEstatico(10)
    for num in [12, 7, 18, 9, 22, 15, 30, 41, 50, 3]:
        v.inserir(num)
    v.imprimir()

    print("\nRemovendo ímpares:")
    v.remover_impares()
    v.imprimir()
    # Saída esperada: [12, 18, 22, 30, 50]

    print("\n=== ETAPA 2: LISTA SIMPLES ===")
    ls = v.exportar_para_lista_simples()
    ls.imprimir()
    # Saída esperada: 12 -> 18 -> 22 -> 30 -> 50 -> None

    print("\nInvertendo in-place:")
    ls.inverter()
    ls.imprimir()
    # Saída esperada: 50 -> 30 -> 22 -> 18 -> 12 -> None

    print("\n=== ETAPA 3: LISTA DUPLAMENTE ENCADEADA ===")
    ld = ls.converter_para_dupla()
    ld.imprimir_frente()
    ld.imprimir_tras()
    # Saída esperada (frente): 50 <-> 30 <-> 22 <-> 18 <-> 12 -> None

    print("\nDividindo ao meio:")
    m1, m2 = ld.split_metade()
    print("Metade 1:")
    m1.imprimir_frente()
    # Saída esperada: 50 <-> 30 -> None
    print("Metade 2:")
    m2.imprimir_frente()
    # Saída esperada: 22 <-> 18 <-> 12 -> None

    print("\n=== ETAPA 4: LISTA CIRCULAR & ELIMINAÇÃO ===")
    lc = ListaCircular.criar_a_partir_de_dupla(m2)
    lc.imprimir_uma_volta()
    # Saída esperada: 22 -> 18 -> 12 -> [volta ao início]

    print("\nEliminando com passo = 2:")
    sobrevivente = lc.girar_e_eliminar(passos=2)
    print(f"Elemento sobrevivente: {sobrevivente}")
    # Saída esperada: 12