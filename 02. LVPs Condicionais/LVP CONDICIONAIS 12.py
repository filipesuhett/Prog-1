#Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

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