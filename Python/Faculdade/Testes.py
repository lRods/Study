"""
    Esqueleto Padrao
"""

def main():
    num = int(input("Digite um numero inteiro e positivo: "))
    while num >= 0:
        fat = calcularFatorial(num)
        print(f"{num}! = {fat}")
        num = int(input("Digite um numero inteiro e positivo: "))


def calcularFatorial(num):
    fatorial = 1
    cont = 1
    while cont <= num:
        fatorial *= cont
        cont += 1
    return fatorial

main()