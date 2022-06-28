'''Faça um programa que receba um opção e um número qualquer, e atenda a opção escolhida, de acordo com o menu, abaixo:

1 - TAMANHO DO NÚMERO
2 - INVERSO DO NÚMERO (DIV e MOD)
3 - É CAPICUA?
4 - É ARMSTRONG?
5 - É PRIMO?
6 - É UM NÚMERO PERFEITO?
7 - BINÁRIO
8 - HEXADECIMAL
9 - MDC ENTRE N E SEU INVERSO
10 - QUANTIDADE DE PRIMOS ENTRE N E SEU INVERSO
11 - SAIR

Será necessário incluir uma validação de dados que só aceite valores de 1 a 11'''

from secundaria import f_tam
from secundaria import f_mdc
from secundaria import f_primo
from secundaria import f_verificaOpcao
from secundaria import f_verificaArmstrong
from secundaria import f_inverte
from secundaria import f_capicua
from secundaria import f_perfeito
from secundaria import f_decToBin
from secundaria import f_decToHex
from secundaria import f_contPrimo

def main():
#n = numero
#m = operação
#s = soma
#c = contador
#0 = verificador
#mi = maior numero
#mn = menor numero
  
  s = 0
  c = 0
  o = True
  m = int(input())

  while (not f_verificaOpcao(m)):
    m = int(input('OPCAO INVALIDA. TENTE OUTRA VEZ:'))
  
  while (m != 11):
    n = int(input())
    s += n
    c += 1

    if (o):
      mi = n
      mn = n
      o = False
    elif (n > mi):
       mi = n
    elif (n < mn):
       mn = n
  
    if (m == 1):
      print(f'TAMANHO DE {n}: {f_tam(n)}')
    elif (m == 2):
      print(f'INVERSO DE {n}: {f_inverte(n)}')
    elif (m == 3):
      if (f_capicua(n)):
        print(f'{n} É CAPICUA')
      else:
        print(f'{n} NÃO É CAPICUA')
    elif (m == 4):
      if (f_verificaArmstrong(n)):
        print(f'{n} É UM NÚMERO ARMSTRONG')
      else:
        print(f'{n} NÃO É UM NÚMERO ARMSTRONG')
    elif (m == 5):
      if (f_primo(n)):
        print(f'{n} É PRIMO')
      else:
        print(f'{n} NÃO É PRIMO')
    elif (m == 6):
      if (f_perfeito(n)):
        print(f'{n} É UM NÚMERO PERFEITO')
      else:
        print(f'{n} NÃO É UM NÚMERO PERFEITO')
    elif (m == 7):
      print(f'{n} EM BINÁRIO: {f_decToBin(n)}')
    elif (m == 8):
      print(f'{n} EM HEXADECIMAL: {f_decToHex(n)}')
    elif (m == 9):
      print(f'MDC ({n},{f_inverte(n)}): {f_mdc(n,f_inverte(n))}')
    elif (m == 10):
      print(f'QUANTIDADE DE PRIMOS ENTRE {n},{f_inverte(n)}: {f_contPrimo(n,f_inverte(n))}')
    m = int(input())
    while (not f_verificaOpcao(m)):
      m = int(input(" OPCAO INVALIDA. TENTE OUTRA VEZ: "))
  return 0

if __name__ == "__main__":
  main()