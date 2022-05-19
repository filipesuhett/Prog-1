#Faça um programa que recebe dois pares de coordenadas e calcule a distância entre os pontos. 

def main():
    
    a = int(input("x1: "))
    b = int(input("x2: "))
    c = int(input("y1: "))
    d = int(input("y2: "))
   
    print("Resultado:", 
      ((a-b)**2+(c-d)**2)**0.5)

if __name__ == "__main__":    
  main()