'''Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo. A última linha que não entrará nos cálculos, contém o valor da idade igual a zero. Calcule e escreva a idade média deste grupo de indivíduos.'''

def main():
  x = True
  z = 0
  a = 0
  
  while (x == True):
    y = int(input(""))
    if(y != 0):
      z += y
      a += 1
    else:  
      x = False

  print(z/a)
  return 0

if __name__ == "__main__":
  main()