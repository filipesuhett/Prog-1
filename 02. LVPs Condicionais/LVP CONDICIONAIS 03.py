#Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor.

def main():
    a = int(input())
    b = int(input())
    if (a>b) :
        print(a-b)
    else:
        print(b-a)
    
    return 0
if __name__ == "__main__":
    main()