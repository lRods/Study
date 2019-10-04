"""
    Exercicio 01 - Baskara
"""
import math

print(" --- Baskara ---\n")
A = float(input("Entre com o valor de A: "))
B = float(input("Entre com o valor de B: "))
C = float(input("Entre com o valor de C: "))

x1 = 0
x2 = 0

delta = (B ** 2) - (4 * A * C)
print("\nDelta = %.2f" % delta)

if delta >= 0:
    x1 = (-B + math.sqrt(delta)) / (2 * A)
    x2 = (-B - math.sqrt(delta)) / (2 * A)

    print("\nRaizes:")
    print("X1 = %.2f" % x1)
    print("X2 = %.2f" % x2)
else:
    print("\nNao a raizes para estes valores.")
