'''Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.'''

def main():
  data = input("")
  d = int(data[0:2])
  m = int(data[3:5])
  a = int(data[6:])
  
  if (m == 1):
    mes = "janeiro"
  elif (m == 2):
    mes = "fevereiro"      
  elif (m == 3):
    mes = "março"      
  elif (m == 4):
    mes = "abril"             
  elif (m == 5):
    mes = "maio"
  elif (m == 6):
    mes = "junho"
  elif (m == 7):
    mes = "julho"
  elif (m == 8):
    mes = "agosto"
  elif (m == 9):
    mes = "setembro"
  elif (m == 10):
    mes = "outubro"
  elif (m == 11):
    mes = "novembro"
  elif (m == 12):
    mes = "dezembro"
            
  print(f'{d} de {mes} de {a}')
            
  return 0

if __name__ == "__main__":
  main()