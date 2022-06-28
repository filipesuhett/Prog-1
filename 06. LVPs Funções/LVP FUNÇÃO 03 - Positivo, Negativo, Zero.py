'''Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento  negativo ou 'Z' se for zero.'''

def f_delay(x):
  arg = 0
  if(x>0):
    arg = "P"
  elif(x==0):
    arg = "Z"
  else:
    arg = "N"
    
  return arg

def main():
  a = int(input("a: "))
  argumento = f_delay(a)
  print(argumento)
  return 0

if __name__ == "__main__":
  main()
