#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

char * strlwr(char * string)
{
  for(int i = 0; i < strlen(string); i++)
  {
    string[i] = tolower(string[i]);
  }
  return string;
}

void main()
{
  int quantidade, taxa;
  char opc[8], dia[16], prato[32];
  float valor, valorTotal, valorDesconto, valorFinal;

  printf("*************************************************\n");
  printf("*                                               *\n");
  printf("*            Restaurante Mosca Frita            *\n");
  printf("*                                               *\n");
  printf("*************************************************\n");   
  printf("*                                               *\n");
  printf("*                                               *\n");
  printf("* Escolha o cardapio que deseja visualizar      *\n");
  printf("*                                               *\n");
  printf("* Dia           Prato do dia          Opcao     *\n");
  printf("* Domingo       Macarronada           Dom       *\n");
  printf("* Quarta        Feijoada              Qua       *\n");
  printf("* Sexta         Peixe Grelhado        Sex       *\n");
  printf("* Sabado        Churrasco             Sab       *\n");
  printf("*                                               *\n"); 
  printf("*************************************************\n");

  printf("Digite a opcao desejada: ");
  scanf("%s", opc);

  if (strcmp(strlwr(opc), "dom") == 0)
  {
    strcpy(dia  , "Domingo");
    strcpy(prato, "Macarronada");
    valor = 12.90;
  }
  else if (strcmp(strlwr(opc), "qua") == 0)
  {
    strcpy(dia  , "Quarta");
    strcpy(prato, "Feijoada");
    valor = 15.50;
  }
  else if (strcmp(strlwr(opc), "sex") == 0)
  {
    strcpy(dia  , "Sexta");
    strcpy(prato, "Peixe Grelhado");
    valor = 11.00;
  }
  else if (strcmp(strlwr(opc), "sab") == 0)
  {
    strcpy(dia  , "Sabado");
    strcpy(prato, "Churrasco");
    valor = 14.30;
  }
  else
  {
    strcpy(dia  , "0");
  }
  

  if (strcmp(dia, "0") != 0) 
  {
    printf("Opcao escolhida: %s\n", dia);
    printf("Prato do dia: %s\n", prato);
    printf("R$ %.2f\n", valor);
    
    printf("Quantidade: ");
    scanf("%d", &quantidade);

    valorTotal = valor * quantidade;
    printf("Valor total a ser pago: %.2f\n\n", valorTotal);

    printf("Desconto? (S/N): ");
    scanf("%s", opc);

    if (strcmp(strlwr(opc), "s") == 0)
    {
      printf("Informe a taxa, em porcentagem, de desconto concedida: ");
      scanf("%d", &taxa);

      valorDesconto = (valorTotal / 100) * taxa;
      valorFinal = valorTotal - valorDesconto;
      printf("\nValor do desconto: %.2f\n", valorDesconto);
    }
    else
    {
      valorFinal = valorTotal;
      printf("\nSem desconto\n");
    }

    printf("Valor a ser pago: %.2f\n", valorFinal);
  }
  else 
  {
    printf("Opcao invalida\n");
  }
}
