'''Um número de Armstrong é um número de N dígitos onde a soma de cada dígito, elevado a N, é igual ao próprio número.

Veja um exemplo com um número de 3 dígitos em base 10:

153 = 13 + 53 + 33 =  1 + 125 + 27 = 153

Escreva um programa que imprima todos os números de Armstrong em base 10 que tenham até 6 dígitos, começando por 1.

Resolva esse exercício utilizando STRING. '''

def main():
  number = 1
  
  while(number != 1000000): 
    soma = 0
    for i in str(number):
      soma += int(i)**(len(str(number)))
    
    if (soma == number):
      print(soma)

    number += 1
  return 0

if __name__ == "__main__":    
  main()