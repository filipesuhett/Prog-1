'''Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.'''

def f_delay(x):
  arg = len(x)
  return arg

def main():
  a = (input("a: "))
  argumento = f_delay(a)
  print(argumento)
  return 0

if __name__ == "__main__":
  main()