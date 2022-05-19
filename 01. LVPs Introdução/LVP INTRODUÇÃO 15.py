#Faça um programa que receba 4 (quatro) notas de um aluno (0 a 100) e apresente a sua média aritmética final.

def main():
  a = 0
  x = 0
  
  for y in range (1,5):
    i = float(input(""))
    a += 1
    x += i
    
  print(x/a)
  return 0

if __name__ == "__main__":
  main()