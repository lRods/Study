
"""
    Exercicio 02 - Maximo
"""

def main():
    letra = input("Digite uma letra: ")
    print(vogal(letra))
    if vogal(letra):
        print("Eh uma vogal")
    else:
        print("Nao eh uma vogal")


def vogal(a):
    if a == 'a'  or a == 'e' or a == 'i' or a == 'o' or a == 'u':
        return True
    else:
        return False

main()