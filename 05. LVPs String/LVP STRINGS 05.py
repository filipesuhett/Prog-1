'''Modifique o programa anterior (APNP LVP STRINGS 4)  de modo que a escada seja invertida.'''

def main():
    nome = input("").upper()
    
    for x in range(len(nome),0,-1):
        print(nome[:x])
        
if __name__ == "__main__":
  main()