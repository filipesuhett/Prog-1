#Faça um Algoritmo que leia 5 valores e escreva no final a soma dos valores positivos e a média dos negativos. 

def main():
  x = 0
  z = 0
  a = 0
  b = 0
  c = 0
  
  while (x < 5):
    y = float(input(""))
    
    if(y > 0):
      a = a + 1
      z = z + y
    else:
      b = b + 1
      c = c + y

    x = x + 1

  print(z , c/b)
  return 0

if __name__ == "__main__":
  main()