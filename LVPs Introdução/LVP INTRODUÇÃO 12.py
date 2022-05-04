#Faça um programa que receba um número inteiro de 3 dígitos e apresente esse número ao contrário. Ex: 123 >> 321  ;  981 >> 189

def main():
    
    a = int(input("Insira um numero: "))
   
    a = str(a)
    
    print(a[::-1])

if __name__ == "__main__":    
  main()