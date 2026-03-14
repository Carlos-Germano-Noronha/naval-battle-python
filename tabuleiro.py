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