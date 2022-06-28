'''Fazer um programa que calcule e escreva o valor de S:
S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50'''

def main():
  z = 1
  a = 1
  b = 0
  
  for y in range (1,51):
    b += z/a
    z += 2
    a += 1

  print(b)
  return 0

if __name__ == "__main__":
  main()