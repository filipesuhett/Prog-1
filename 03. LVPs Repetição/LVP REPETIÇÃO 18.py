'''Fazer um programa que calcule e escreva o valor de S:
S = (37 x 38)/1 + (36 x 37)/2 + (35 x 36)/3 + ... + (1 x 2)/37'''

def main():
  z = 37
  a = 38
  x = 1
  b = 0
  
  for y in range (1,38):
    b += (z*a)/x
    z -= 1
    a -= 1
    x += 1

  print(b)
  return 0

if __name__ == "__main__":
  main()