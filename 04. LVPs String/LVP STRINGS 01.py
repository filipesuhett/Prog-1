'''Faça um programa que leia 2 strings e informe se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.'''

def main():
    y = input("")
    x = input("")
  
    if(len(x) == len(y)):
        print("MESMO TAMANHO")
    else:
        print("TAMANHO DIFERENTE")
        
    if(x == y):
        print("CONTEÚDO IGUAL")
    else:
        print("CONTEÚDO DIFERENTE")    
     

if __name__ == "__main__":
  main()