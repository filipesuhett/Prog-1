'''Faça um programa que conte a incidência de um determinado número [0-9] dentro de um intervalo de valores, começando em 0 e o fim do intervalo determinado pelo usuário.'''

def f_conta(num,inci):
  cont = 0
  quant = 0
  
  while(inci >= cont):
    num = str(num)
    cont = str(cont)
    for x in range(len(cont)):
      if(num == cont[x]):
        quant += 1
    num = int(num)
    cont = int(cont)
    cont += 1
  return quant

def main():
  num = int(input())
  inci = int(input())
  
  print(f_conta(num,inci))
    
  return 0

if __name__ == "__main__":
  main()