'''Faça um Programa que leia números até que o usuário não queira mais digitar os números. No final escrever a soma dos valores positivos e a média dos valores negativos.  (o usuário digitará a letra s para continuar informando dados e n quando quiser parar)'''

def main():
  y = input("").upper()
  z = 0
  c = 0
  x = 0
  
  while (y == "S"):
    b = int(input())
    y = input("").upper()
      
    if(b > 0):
      z += b
    else:
      c += b
      x += 1

  print(z , c/x)
  return 0

if __name__ == "__main__":
  main()