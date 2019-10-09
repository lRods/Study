"""
    Exercicio 04 - Pessoas
"""

fem = 0
mas = 0
nome = input("Nome da pessoa: ").lower()
while nome != "fim":
    sexo = input("Sexo da pessoa (M/F): ").lower()
    if sexo == 'm':
        mas += 1
    else:
        fem +=1
    nome = input("Nome da pessoa: ").lower()
print("\nQuantidade masculino: ", mas)
print("Quantidade feminino: ", fem)
