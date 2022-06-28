'''Modifique o programa anterior (APNP LVP STRINGS 3) de forma a mostrar o nome em formato de escada.'''

def main():
    nome = input("").upper()
    
    for x in range(0, len(nome)+1):
        print(nome[x:])
        
if __name__ == "__main__":
  main()