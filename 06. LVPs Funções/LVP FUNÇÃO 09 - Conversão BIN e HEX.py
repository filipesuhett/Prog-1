'''Faça um programa que recebe n números inteiros maiores ou iguais a zero. Considere que a entrada de encerra quando um número menor que zero for informado pelo usuário.

- Faça uma função externa que receba um número inteiro maior ou igual a zero na base 10 e retorne um número inteiro maior ou igual a zero que representa, na base 2 (binário), o número na base 10 fornecido como entrada para esta função.

- Faça uma função externa que receba um número inteiro maior ou igual a zero na base 10 e retorne um número inteiro maior ou igual a zero que representa, na base 16 (hexadecimal), o número na base 10 fornecido como  entrada para esta função.

- Para cada número LIDO imprima seu respectivo valor na base 2 e na base 16, conforme modelo abaixo. '''

def f_decToBin(n):
  s = " "
  while (n > 0):
    resto = n % 2
    s = str(resto) + s
    n = n // 2
  return s

def f_hex(resto):
  s = 'ABCDEF'
  return s[resto - 10]

def f_hex2(r):
  if ( r == 10):
    return "A"
  if ( r == 11):
    return "B"
  if ( r == 12):
    return "C"
  if ( r == 13):
    return "D"
  if ( r == 14):
    return "E"
  if ( r == 15):
    return "F"


def f_decToHex(n):
  s = ""
  while(n > 0):
    resto = n % 16
    if (resto < 10):
      s = str(resto) + s
    else:
      s = f_hex(resto) + s
    n = n // 16
  return s

def main():
  n = int(input())
  while (n >= 0):
    print(f'DEC={n} BIN={f_decToBin(n)} HEX={f_decToHex(n)}')
    n = int(input())
  return 0


if __name__=="__main__":
  main()