#Tendo como dados de entrada os sexo, o peso e a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

#- para homens: (72.7 * h) – 58
#- para mulheres: (62.1 * h) – 44.7

#E que calcule seu IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC o peso dividido pelo quadrado da altura

#A condição do indivíduo segue a classificação da tabela abaixo:

#IMC	Classificação
#Abaixo de 17	MUITO ABAIXO DO PESO
#Entre 17 e 18,49	ABAIXO DO PESO
#Entre 18,50 e 24,99	PESO NORMAL
#Entre 25 e 29,99	ACIMA DO PESO
#Entre 30 e 34,99	OBESIDADE I
#Maior que 34,99	OBESIDADE II (SEVERA)
#Elabore um programa que apresente o peso ideal de uma pessoa e sua classificação de IMC

def main():
    
    a = input("")
    peso = int(input(""))
    altura = float(input(""))

    x = peso/altura**2

    if ("M"==a):
      print(f'PESO IDEAL:{(72.7 * altura) - 58:.2f}')
    else:
      print(f'PESO IDEAL:{(62.1 * altura) - 44.7:.2f}')

    
    print(f'IMC: {x:.2f}')


    if (x<=17):
      print("MUITO ABAIXO DO PESO")
    elif (17<x<18.49):
      print("ABAIXO DO PESO")
    elif (18.50<x<24.99):
      print("PESO NORMAL")
    elif (25<x<29.99):
      print("ACIMA DO PESO")
    elif (30<x<34.99):
      print("OBESIDADE I")
    else:
      print("OBESIDADE II (SEVERA)")

      
    
    return 0

if __name__ == "__main__":    
  main()