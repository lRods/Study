"""
    Jogo do NIN
    Rodrigo Maia - N3825H-8
"""

def main():
    print("Bem-vindo ao jogo do NIM!")
    print("Escolha: ")
    print("1 - Para jogar uma partida isolada\n2 - Para jogar um campeonato")
    opc = int(input("~ "))

    if opc == 1:
        print("\nVoce escolheu uma partida isolada!\n")
        partida()
    else:
        print("\nVoce escolheu um campeonato!\n")
        for i in range(1, 4):
            print(f"***** Rodada {i} *****\n")
            partida()

        print("***** Fim do campeonato! *****\n")
        print("Placar: Voce 0 X 3 Computador\n")


def plural(num):
    if num > 1:
        return f"{num} pecas"
    else:
        return "uma peca"

def computador_escolhe_jogada(m, n):
    count = m
    while count >= 1:
        if (n - count) % (m + 1) == 0:
            print(f"\nO computador tirtou {plural(count)}.")
            return count
        else:
            count -= 1

def usuario_escolhe_jogada(m, n):
    while True:
        quant = int(input("\nQuantas pecas voce quer tirar? "))
        if quant > 0 and quant <= m:
            print(f"Voce tirou {plural(quant)}.")
            return quant
        else:
            print("Oops! Jogada invalida! Tente de novo.")

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
