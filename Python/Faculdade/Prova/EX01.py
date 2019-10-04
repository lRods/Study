"""
    Calculos
"""
import math

num = int(input("Informe um numero: "))
if num < 0:
    print("Numero Negativo")
else:
    print("Opcoes:\n"
        "1 - Quadrado\n"
        "2 - Raiz Quadrada\n"
        "3 - Cubo\n"
        "4 - Soma de todas as operacoes acima")
    opc = int(input("Digite sua opcao: "))

    if opc == 1:
        res = math.pow(num, 2)
    elif opc == 2:
        res = math.sqrt(num)
    elif opc == 3:
        res = math.pow(num, 3)
    elif opc == 4:
        res = math.pow(num, 2) + math.sqrt(num) + math.pow(num, 3)
    else:
        res = -1

    if res == -1:
        print("Opcao invalida")
    else:
        print("Resultado = %.2f" % res)
