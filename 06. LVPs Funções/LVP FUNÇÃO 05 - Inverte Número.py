'''Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721'''

def main():
    
    a = int(input("Insira um numero: "))
   
    a = str(a)
    
    print(a[::-1])

if __name__ == "__main__":    
  main()