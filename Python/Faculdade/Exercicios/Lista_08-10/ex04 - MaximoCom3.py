"""
    Exercicio 03 - Maximo com 3
"""

def main():
    print(maximo(30,14, 10))
    print(maximo(0,-1, 1))


def maximo(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

main()