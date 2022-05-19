#Faça um programa que receba a idade de uma pessoa, em dias, e apresente a idade dessa pessoa em anos, meses e dias. Considere um ano com 365 dias e um ano com 30 dias.

def main():
    
    a = int(input("insira o total de dias: "))
    
    x = a//365 
    y = a%365
    z = y//30
    p = y%30
    
    r = [x, z, p]
    
    print(r)

if __name__ == "__main__":    
  main()