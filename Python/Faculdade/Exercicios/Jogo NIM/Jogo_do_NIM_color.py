"""
    Jogo do NIN
    Rodrigo Maia - N3825H-8
"""

def main():
    print("\033[1mBem-vindo ao \033[34mjogo do NIM\033[0;0m!")
    print("Escolha: ")
    print("1 - Para jogar uma partida isolada\n2 - Para jogar um campeonato")
    opc = int(input("~ "))

    if opc == 1:
        print("\nVoce escolheu uma partida isolada!\n")
        partida()
    else:
        print("\nVoce escolheu um campeonato!\n")
        for i in range(1, 4):
            print(f"\033[1m***** Rodada {i} *****\033[0;0m\n")
            partida()

        print("\033[1m***** Fim do campeonato! *****\033[0;0m\n")
        print("\033[37m\033[41m VOCE \033[0;0m\033[1m 0 X 3 \033[0;0m\033[44m\033[37m COMPUTADOR \033[0;0m\n")


def plural(num):
    if num > 1:
        return f"\033[1m{num} pecas\033[0;0m"
    else:
        return "\033[1muma peca\033[0;0m"

def computador_escolhe_jogada(m, n):
    print("\n\033[44m\033[37m COMPUTADOR \033[0;0m")
    count = m
    while count >= 1:
        if (n - count) % (m + 1) == 0:
            print(f"O computador tirtou {plural(count)}.")
            return count
        else:
            count -= 1

def usuario_escolhe_jogada(m, n):
    print("\n\033[41m\033[37m VOCE \033[0;0m")
    while True:
        quant = int(input("Quantas pecas voce quer tirar? "))
        if quant > 0 and quant <= m:
            print(f"Voce tirou {plural(quant)}.")
            return quant
        else:
            print("Oops! Jogada invalida! Tente de novo.\n")

def partida():
    n = int(input("Quantas pecas? "))
    m = int(input("Limite de pecas por rodada? "))

    # Jogador -> 0 = computador | 1 = Usuario
    if n % (m+1) == 0:
        print("\nVoce comeca!")
        jogador = 1
    else:
        print("\nComputador comeca!")
        jogador = 0

    while n > 0:
        if jogador == 1:
            n -= usuario_escolhe_jogada(m, n)
            jogador = 0
        else:
            n -= computador_escolhe_jogada(m, n)
            jogador = 1
        if n != 0:
            print(f"Agora restam {plural(n)} no tabuleiro.")

    print("Fim do jogo! O computador ganhou!\n")

main()
