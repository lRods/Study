"""
    Exercicio 05 - Numeros Primos
"""

def main():
    num = int(input("Digite um numero inteiro: "))
    while num > 0:
        if primo(num):
            print("Primo")
        else:
            print("Nao primo")
        num = int(input("Digite um numero inteiro: "))

def primo(x):
    if x == 1:
        return False
    count = 2
    primo = True
    while count < x:
        if x % count == 0:
            primo = False
            break
        count += 1
    return primo

main()