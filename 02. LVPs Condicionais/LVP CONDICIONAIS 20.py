#Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.

def main():

  a = int(input(""))            
  b = int(input(""))
  c = int(input(""))
  d = int(input(""))

  if (a>b) and (c>d):
    print(a+d, b*c)
  elif (a<b) and (c<d):
    print(b+c, d*a)
  elif (b>a) and (c>d):
    print(b+d, a*c)
  else:
    print(a+c, b*d)
  
  return 0
if __name__ == "__main__":
  main()