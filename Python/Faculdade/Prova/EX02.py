"""
    Calculo de Reajuste Salarial
"""

codigo = input("Entre com o codigo do funcionario: ")

cargo = False
if codigo == '10':
    cargo = "Ajudante"
    aumento = 1.40
elif codigo == '20':
    cargo = "Pedreiro"
    aumento = 1.35
elif codigo == '30':
    cargo = "Mestre de obras"
    aumento = 1.30
elif codigo == '40':
    cargo = "Arquiteto"
    aumento = 1.25
elif codigo == '50':
    cargo = "Engenheiro"
    aumento = 1

if cargo:
    salario = float(input("Entre com o salario deste funcionario: "))

    reajuste = salario * aumento
    valorAumento = reajuste - salario
    print("\nCargo: ", cargo)
    print("Valor do aumento: R$ %.2f" % valorAumento)
    print("Novo salario: R$ %.2f" % reajuste)
else:
    print("Codigo invalido")
