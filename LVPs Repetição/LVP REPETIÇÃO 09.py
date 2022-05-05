#Faça um Algoritmo que leia 5 valores inteiros e escreva no final a média dos valores lidos.

def main():
  x = 0
  z = 0
  
  while (x < 5):
      y = int(input(""))
      z = z + y
      x = x + 1

  print(z/x)
  return 0

if __name__ == "__main__":
  main()