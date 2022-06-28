'''Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

a. quantos espaços em branco existem na frase.
b. quantas vezes aparecem as vogais a, e, i, o, u.'''

def main():
    frase = input("").upper()
    branco = 0
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    
    for x in range(len(frase)):
        if (frase[x] == " "):
            branco += 1
        elif (frase[x] == "A"):
            a += 1
        elif (frase[x] == "E"):
            e += 1
        elif (frase[x] == "I"):
            i += 1    
        elif (frase[x] == "O"):
            o += 1    
        elif (frase[x] == "U"):
            u += 1
            
    print(f'ESPAÇOS EM BRANCO = {branco}')
    print(f'A = {a}')
    print(f'E = {e}')
    print(f'I = {i}')
    print(f'O = {o}')
    print(f'U = {u}')
            
    return 0

if __name__ == "__main__":
  main()