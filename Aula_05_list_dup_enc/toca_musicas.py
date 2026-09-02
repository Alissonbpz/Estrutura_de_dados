# =====================================================================
# 1. NÓ DE MÚSICA
# =====================================================================

class NodeMusica:

    def __init__(self, titulo: str, artista: str, duracao: int):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao  # em segundos
        self.anterior = None
        self.proximo = None


# =====================================================================
# 2. TAD DO PLAYER CIRCULAR DUPLAMENTE ENCADEADO
# =====================================================================

class PlayerCircular:

    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.faixa_atual = None

    def esta_vazia(self) -> bool:
        return self.cabeca is None

    def adicionar_musica(self, titulo: str, artista: str, duracao: int):
        """Insere no fim mantendo o anel fechado."""

        nova_musica = NodeMusica(titulo, artista, duracao)

        if self.esta_vazia():

            self.cabeca = nova_musica
            self.cauda = nova_musica
            self.faixa_atual = nova_musica

        else:

            nova_musica.anterior = self.cauda
            self.cauda.proximo = nova_musica
            self.cauda = nova_musica

        # Manter o anel fechado
        self.cabeca.anterior = self.cauda
        self.cauda.proximo = self.cabeca

    def tocar_atual(self):
        """Exibe a faixa em reprodução."""

        if not self.esta_vazia():

            print(
                f"▶ Tocando: {self.faixa_atual.titulo} - "
                f"{self.faixa_atual.artista} "
                f"({self.faixa_atual.duracao}s)"
            )

    def proxima_musica(self):
        """Avança para a próxima música em ciclo."""

        if not self.esta_vazia():

            self.faixa_atual = self.faixa_atual.proximo

            print(
                f"⏭ Avançando: {self.faixa_atual.titulo} - "
                f"{self.faixa_atual.artista} "
                f"({self.faixa_atual.duracao}s)"
            )

    def voltar_musica(self):
        """Retorna para a música anterior em ciclo."""

        if not self.esta_vazia():

            self.faixa_atual = self.faixa_atual.anterior

            print(
                f"⏮ Voltando: {self.faixa_atual.titulo} - "
                f"{self.faixa_atual.artista} "
                f"({self.faixa_atual.duracao}s)"
            )

    def exibir_playlist(self):
        """Percorre exatamente 1 ciclo completo."""

        if not self.esta_vazia():

            atual = self.cabeca
            contador = 1

            print("=== FILA DE REPRODUÇÃO (LOOP ATIVO) ===")

            while True:

                if atual == self.faixa_atual:

                    print(
                        f"{contador}. [TOCANDO AGORA] "
                        f"{atual.titulo} - {atual.artista} "
                        f"({atual.duracao}s)"
                    )

                else:

                    print(
                        f"{contador}. "
                        f"{atual.titulo} - {atual.artista} "
                        f"({atual.duracao}s)"
                    )

                contador += 1
                atual = atual.proximo

                if atual == self.cabeca:
                    break

            print("=======================================")

    def remover_musica(self, titulo: str) -> bool:
        """Remove o nó e refaz a costura circular."""

        if self.esta_vazia():
            return False

        atual = self.cabeca

        while True:

            if atual.titulo == titulo:

                # Única música na playlist
                if atual == self.cabeca and atual == self.cauda:

                    self.cabeca = None
                    self.cauda = None
                    self.faixa_atual = None

                else:

                    # Refaz as ligações
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior

                    # Se removeu a cabeça
                    if atual == self.cabeca:
                        self.cabeca = atual.proximo

                    # Se removeu a cauda
                    if atual == self.cauda:
                        self.cauda = atual.anterior

                    # Se removeu a música que estava tocando
                    if atual == self.faixa_atual:
                        self.faixa_atual = atual.proximo

                    # Garantir o anel fechado
                    self.cabeca.anterior = self.cauda
                    self.cauda.proximo = self.cabeca

                print(
                    f"[!] Música '{titulo}' removida "
                    f"da playlist circular."
                )

                return True

            atual = atual.proximo

            if atual == self.cabeca:
                break

        print(
            f"[!] Música '{titulo}' não encontrada "
            f"na playlist circular."
        )

        return False


# =====================================================================
# 3. TESTES DE VALIDAÇÃO
# =====================================================================

if __name__ == "__main__":

    player = PlayerCircular()

    print("--- 1. Adicionando 3 faixas à Playlist Circular ---")

    player.adicionar_musica(
        "Bohemian Rhapsody",
        "Queen",
        354
    )

    player.adicionar_musica(
        "Hotel California",
        "Eagles",
        391
    )

    player.adicionar_musica(
        "Billie Jean",
        "Michael Jackson",
        294
    )

    player.exibir_playlist()


    print("\n--- 2. Testando Loop Contínuo para Frente (Avançar 4 vezes) ---")

    player.tocar_atual()

    player.proxima_musica()  # Hotel California
    player.proxima_musica()  # Billie Jean
    player.proxima_musica()  # Bohemian Rhapsody
    player.proxima_musica()  # Hotel California


    print("\n--- 3. Testando Loop para Trás (Voltar 2 vezes) ---")

    player.voltar_musica()  # Bohemian Rhapsody
    player.voltar_musica()  # Billie Jean


    print("\n--- 4. Removendo faixa da cabeça em lista circular ---")

    player.remover_musica("Bohemian Rhapsody")

    player.exibir_playlist()

# =====================================================================
# 4. SAIDA ESPERADA
# =====================================================================

"""--- 1. Adicionando 3 faixas à Playlist Circular ---
=== FILA DE REPRODUÇÃO (LOOP ATIVO) ===
1. [TOCANDO AGORA] Bohemian Rhapsody - Queen (354s)
2. Hotel California - Eagles (391s)
3. Billie Jean - Michael Jackson (294s)
=======================================

--- 2. Testando Loop Contínuo para Frente (Avançar 4 vezes) ---
▶ Tocando: Bohemian Rhapsody - Queen (354s)
⏭ Avançando: Hotel California - Eagles (391s)
⏭ Avançando: Billie Jean - Michael Jackson (294s)
⏭ Avançando: Bohemian Rhapsody - Queen (354s) [REINICIOU O CICLO]
⏭ Avançando: Hotel California - Eagles (391s)

--- 3. Testando Loop para Trás (Voltar 2 vezes) ---
⏮ Voltando: Bohemian Rhapsody - Queen (354s)
⏮ Voltando: Billie Jean - Michael Jackson (294s) [PULOU PARA A ÚLTIMA]

--- 4. Removendo faixa da cabeça em lista circular ---
[!] Música 'Bohemian Rhapsody' removida da playlist circular.
=== FILA DE REPRODUÇÃO (LOOP ATIVO) ===
1. Hotel California - Eagles (391s)
2. [TOCANDO AGORA] Billie Jean - Michael Jackson (294s)
======================================="""