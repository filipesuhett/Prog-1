'''Tem-se um conjunto de dados contendo o sexo (masculino, feminino) e a altura de 5 pessoas. Fazer um algoritmo que calcule e escreva:
- a maior e a menor altura do grupo;
- a média de altura das mulheres;
- a quantidade de homens;'''

def main():
  maioralt = 0
  menoralt = 3
  mediam = 0
  quanth = 0
  somam = 0
  
  for i in range (1,6):
    sexo = input("").upper()
    altura = float(input(""))

    if ("M" == sexo):
      quanth += 1
      if (altura > maioralt):
        maioralt = altura
      elif (altura < menoralt):
        menoralt = altura  
    else:
      mediam += 1
      somam += altura
      if (altura > maioralt):
        maioralt = altura
      elif (altura < menoralt):
        menoralt = altura
  
  print(f'A Maior Altura é: {maioralt:.2f}')
  print(f'A Menor Altura é: {menoralt:.2f}')
  print(f'A Média da Altura de todas as mulheres é: {somam/mediam:.2f}')
  print(f'A Quantida de Homens é: {quanth:.2f}')
  
  return 0

if __name__ == "__main__":
  main()