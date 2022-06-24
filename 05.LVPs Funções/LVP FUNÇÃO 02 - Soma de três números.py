'''Faça um programa que leia três número e, a partir de uma função, informe o resultado da soma, dos mesmos.'''

def f_delay(x,y,z):
  somaF = x + y + z
  return somaF

def main():
  a = int(input("a: "))
  b = int(input("b: "))
  c = int(input("c: "))
  soma = f_delay(a,b,c)
  print(soma)
  return 0

if __name__ == "__main__":
  main()