'''Um número de Armstrong é um número de N dígitos onde a soma de cada dígito, elevado a N, é igual ao próprio número.

Veja um exemplo com um número de 3 dígitos em base 10:

153 = 1**3 + 5**3 + 3**3 =  1 + 125 + 27 = 153

Escreva um programa que imprima todos os números de Armstrong em base 10 que tenham até 6 dígitos, começando por 1.

Resolva esse exercício utilizando, apenas DIV e MOD. '''

def f_tam(a):
  c = 0
  while (a > 0):
    c += 1
    a = a // 10
  return c

def f_armstrong(a):
  p = f_tam(a)
  s = 0
  while (a > 0):
    r = a % 10
    s += r ** p
    a = a // 10
  return s

def f_verificaArmstrong(a):
  return a == f_armstrong(a)

def main():
  for a in range(1,1000000):
    if (f_verificaArmstrong(a)):
      print(a)
  return 0

if __name__ == "__main__":
  main()
