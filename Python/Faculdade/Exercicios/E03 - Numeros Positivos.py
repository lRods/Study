"""
    Exercicio 03 - Numeros Positivos
"""
import os

print(" --- Numeros Positivos ---\n")

quant = 0
num = int(input("Numero: "))
while num > 0:
    quant += 1
    num = int(input("Numero: "))

# os.system("tput cuu1; tput dl1 ")
print("Voce digitou %d numeros positivos." % quant)