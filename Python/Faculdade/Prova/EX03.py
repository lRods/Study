"""
    Restaurante Mosca Frita
"""

print("************************************************\n" 
      "*                                              *\n" 
      "*           Restaurante Mosca Frita            *\n"
      "*                                              *\n"
      "************************************************\n"
      "*                                              *\n"
      "*                                              *\n"
      "* Escolha o cardapio que deseja visualizar     *\n"
      "*                                              *\n"
      "* Dia           Prato Principal       Opcao    *\n"
      "* Domingo       Macarronada           Dom      *\n"
      "* Quarta        Feijoada              Qua      *\n"
      "* Sexta         Peixe Grelhado        Sex      *\n"
      "* Sabado        Churrasco             Sab      *\n"
      "*                                              *\n"
      "************************************************")

opc = input("Digite a opcao desejada: ")

dia = False
if opc.lower() == "dom":
    dia = "Domingo"
    prato = "Macarronada"
    valor =  12.90
else:
    if opc.lower() == "qua":
        dia = "Quarta"
        prato = "Feijoada"
        valor = 15.50
    else:
        if opc.lower() == "sex":
            dia = "Sexta"
            prato = "Peixe Grelhado"
            valor = 11.00
        else:
            if opc.lower() == "sab":
                dia = "Sabado"
                prato = "Churrasco"
                valor = 14.30

if dia:
    print("Opcao escolhida: ", dia)
    print("Prato do dia: ", prato)
    print("R$ %.2f" % valor)
    quantidade = int(input("Quantidade: "))
    valorTotal = quantidade * valor
    print("Valor a ser pago: %.2f\n" % valorTotal)

    desconto = input("Desconto? (S/N): ")
    if desconto.lower() == 's':
        taxa = int(input("Informe a taxa, em porcentagem, de desconto concedida: "))
        valorDesconto = (valorTotal/100) * taxa
        valorFinal = valorTotal - valorDesconto

        print("\nValor do desconto: %.2f" % valorDesconto)
    else:
        valorFinal = valorTotal
        print("\nSem desconto")

    print("Valor a ser pago: %.2f" % valorFinal)
else:
    print("~ Dia da semana invalido")
