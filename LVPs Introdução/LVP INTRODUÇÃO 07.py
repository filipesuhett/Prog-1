#Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

def main():
    
    a = int(input("Sálario: "))
    b = int(input("Reajuste: "))
    
    x = b/100
    y = x*a
    z = y+a
    print(z)
    
    return 0

if __name__ == "__main__":    
  main()