"""
    Exercicio 02 - Maximo
"""

def main():
    print(maximo(3,4))
    print(maximo(0,-1))


def maximo(x, y):
    if x > y:
        return x
    else:
        return y

main()