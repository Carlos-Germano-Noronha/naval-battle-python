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