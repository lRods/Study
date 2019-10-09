"""
    Exercicio 01 - Baskara
"""
import math

def main():
    print(" --- Baskara ---\n")
    A = float(input("Entre com o valor de A: "))
    B = float(input("Entre com o valor de B: "))
    C = float(input("Entre com o valor de C: "))

    x = baskara(A, B, C)

    if x != -1:
        print("\nRaizes:")
        print("X1 = %.2f" % x[0])
        print("X2 = %.2f" % x[1])
    else:
        print("\nNao a raizes para estes valores.")

def baskara(A, B, C):
    delta = (B ** 2) - (4 * A * C)

    if delta >= 0:
        x1 = (-B + math.sqrt(delta)) / (2 * A)
        x2 = (-B - math.sqrt(delta)) / (2 * A)

        return x1, x2
    else:
        return -1

main()