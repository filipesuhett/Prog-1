'''Faça um programa que leia dois número e, a partir de uma função, informe o resultado da soma, dos mesmos.'''

def f_delay(x,y):
  somaF = x + y
  return somaF

def main():
  a = int(input("a: "))
  b = int(input("b: "))
  soma = f_delay(a,b)
  print(soma)
  return 0

if __name__ == "__main__":
  main()