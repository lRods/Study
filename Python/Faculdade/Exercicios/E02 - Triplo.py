"""
    Exercicio 02 - Triplo
"""

print(" --- Triplo ---\n")

while True:
    num = int(input("Entre com um numero: "))
    if num == -999:
        break
    else:
        num *= 3
        print("Triplo = %d\n" % num)

print("\n --- FIM ---")
