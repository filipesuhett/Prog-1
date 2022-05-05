#Faça um Algoritmo que leia 5 valores inteiros e escreva no final a soma dos valores lidos.

def main():
  x = 5
  z = 0
  
  while (x > 0):
      y = int(input(""))
      z = z + y
      x = x - 1

  print(z)
  return 0

if __name__ == "__main__":
  main()