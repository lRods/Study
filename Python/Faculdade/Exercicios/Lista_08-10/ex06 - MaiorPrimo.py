"""
    Exercicio 06 - Maior Primo
"""

def main():
    num = int(input("Digite um numero inteiro: "))
    while num > 0:
        print("Maior primo: ", maior_primo(num))
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

def maior_primo(x):
    count = 2
    maior = "-"
    while count <= x:
        if primo(count):
            maior = count
        count += 1
    return maior

main()