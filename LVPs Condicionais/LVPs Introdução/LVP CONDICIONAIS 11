#Efetuar a leitura de três valores (variáveis A, B e C) e efetuar o cálculo da equação completa de segundo grau, apresentando as duas raízes, se para os valores informados for possível efetuar o referido cálculo. Lembre-se de que a variável A deve ser diferente de zero.

def main():
    
    a = float(input(" "))
    b = float(input(" "))
    c = float(input(" "))

    x = (b**2-4*a*c)
    
    y = x**(1/2)
    
    x1 = (-b-y)/(2*a)
    
    if(x > 0):
      x1 = (-b-y)/(2*a)
      x2 = (-b+y)/(2*a)
      print(x2,x1)
    elif(x == 0):
      print(x1)
    else:  
      print("Não possui raiz")
      
    return 0

if __name__ == "__main__":    
  main()