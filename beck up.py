import random

class Tabuleiro:
    def __init__(self, tamanho = 15):
        self.tamanho = tamanho
        self.tabuleiro = []
        self.alternativas = []
        self.navios = []
        self.gerar_tabuleiro()
        self.posicoes_atacadas = []
        self.selecionar_navios()
        self.navios_destriodos = []


    def gerar_tabuleiro(self):
        self.tabuleiro = []
        for i in range(1, self.tamanho + 1):
            linha = []
            for j in range(1, self.tamanho + 1):
                linha.append('O')
                self.alternativas.append((i, j))
            self.tabuleiro.append(linha)

    def selecionar_navios(self,):
        while len(self.navios) < 20:
            linhas, colunas = random.choice(self.alternativas)
            if colunas + 1 <= self.tamanho:
                corrigir = (linhas, colunas + 1)
                if (linhas,colunas) not in self.navios and corrigir not in self.navios:
                    self.navios.append((linhas,colunas))
                    self.navios.append((linhas,colunas + 1))
                    self.alternativas.remove((linhas, colunas))
                    self.alternativas.remove((corrigir))

    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print(" ".join(linha))

    def mostrar_navios(self):
        for linha, coluna in self.navios:
            if(linha, coluna) in self.navios_destriodos:
                self.tabuleiro[linha - 1] [coluna - 1] = "X"
            else:
                self.tabuleiro[linha - 1][coluna - 1] = "N"
        self.imprimir_tabuleiro()

    def atacar(self, linha, coluna, tabuleiro_inimigo):
        if(linha == -1 and coluna == -1) or (linha == -2 and coluna == -2): #sei que há redundancia, entre o if e o swith case
            match(linha, coluna):
                case(-1, -1):
                    self.mostrar_navios()
                case(-2, -2):
                    tabuleiro_inimigo.tabuleiro_inimigo()
            return
        if (linha, coluna) in self.posicoes_atacadas:
            return "Posição já atacada!"
        else:
            self.posicoes_atacadas.append((linha, coluna))
            navio_destruido = False
            for (navio_linha, navio_coluna) in self.navios:
                if (linha, coluna) == (navio_linha, navio_coluna):
                    self.tabuleiro[navio_linha - 1][navio_coluna - 1] = "X"
                    if (navio_linha, navio_coluna + 1) in self.navios:
                        self.tabuleiro[navio_linha - 1][navio_coluna] = "X"
                        self.navios_destriodos.append((linha, coluna +1))
                    elif (navio_linha, navio_coluna - 1) in self.navios:
                        self.tabuleiro[navio_linha - 1][navio_coluna - 2] = "X"
                        self.navios_destriodos.append((linha, coluna - 1))
                    self.navios_destriodos.append((navio_linha, navio_coluna))
                    navio_destruido = True
                    break
        if navio_destruido:
            return "Acertou, o Navio foi destruido"
        else:
            self.tabuleiro[linha - 1][coluna - 1] = "-"
            return "Errou"

    def tabuleiro_inimigo(self):
        mostrar_inimigo = [['O' for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        for linha, coluna in self.navios:
            mostrar_inimigo[linha - 1][coluna - 1] = "N"
            for linha, coluna in self.posicoes_atacadas:
                mostrar_inimigo[linha - 1][coluna - 1] = "-"
            if self.posicoes_atacadas in self.navios:
                self.navios_destriodos.append((linha,coluna))
            for linha, coluna in self.navios_destriodos:
                mostrar_inimigo[linha -1] [coluna -1] = "X"
        for linha in mostrar_inimigo:
            print(" ".join(linha))

    def tem_navios(self):
        return len(self.navios) > 0
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
from jogador import Jogador
import random
def jogo():
    jogador1 = Jogador("Professor")
    jogador2 = Jogador("Computador muito forte e potente")
    vez_jogador1 = False
    jogador1.tabuleiro.selecionar_navios()
    jogador2.tabuleiro.selecionar_navios()
    pc_atacou = []
    while jogador1.tem_navios() and jogador2.tem_navios():
        print('')
        if vez_jogador1:
            while True:
                linha, coluna = map(int, input(
                    f"{jogador1.nome}, insira as coordenadas para atacar (linha coluna): ").split())
                resultado = jogador1.atacar(jogador2, linha, coluna)
                if resultado != "Posição já atacada!":
                    break
            if resultado == "Errou":
                vez_jogador1 = False

        else:
            while True:
                linha = random.randint(1, 15)
                coluna = random.randint(1, 15)
                if (linha, coluna) not in pc_atacou:
                    pc_atacou.append((linha, coluna))
                    resultado = jogador2.atacar(jogador1, linha, coluna)
                    break
            if resultado == "Errou":
                vez_jogador1 = True
        if not jogador2.tem_navios():
            print(f"{jogador2.nome} perdeu! {jogador1.nome} venceu!")
            break
        elif not jogador1.tem_navios():
            print(f"{jogador1.nome} perdeu! {jogador2.nome} venceu!")
            break
    jogar_novamente = input('Jogar novamente? (S/N)').strip().lower()
    while jogar_novamente not in ['s', 'n']:
        print('Não entendi!')
        jogar_novamente = input('Jogar novamente? (S) para sim, (N) para não)').strip().lower()
    if jogar_novamente == 's':
        jogo()
    else:
        print("Obrigado por jogar")

if __name__ == "__main__":
    jogo()