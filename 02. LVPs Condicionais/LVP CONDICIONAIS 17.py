#Tendo como dados de entrada a altura e o sexo (M ou F) de uma pessoa, calcule e mostre seu peso ideal, utilizando as seguintes fórmulas: - para sexo masculino: peso ideal = (72.7 * altura) - 58 – para sexo feminino: peso ideal = (62.1 * altura) - 44.7

def main():

  a = (input("a: "))            
  b = float(input("b: "))

  if (a=="M"):
    print((72.7*b)-58)
  else:
    print((62.1*b)-44.7)
  
  return 0
if __name__ == "__main__":
  main()