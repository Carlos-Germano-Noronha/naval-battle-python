from tabuleiro import Tabuleiro

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.tabuleiro = Tabuleiro()

    def atacar(self, outro_jogador, linha, coluna):
        if linha == -1 and coluna == -1:
            self.tabuleiro.mostrar_navios()
            resultado = 'Seu Tabuleiro'
            print(resultado)
        elif linha == -2 and coluna == -2:
            outro_jogador.tabuleiro.tabuleiro_inimigo()
            resultado = 'Tabuleiro do Computador'
            print(resultado)

        else:
            print(f"{self.nome} atacou a posição ({linha}, {coluna})!")
            resultado = outro_jogador.tabuleiro.atacar(linha, coluna, outro_jogador.tabuleiro)
            print(resultado)

        return resultado

    def tem_navios(self):
        return self.tabuleiro.tem_navios()