'''Fazer um programa que calcule e escreva o valor de S:
S = 1/1 – 2/4 + 3/9 – 4/16 + 5/25 – 6/36 ... - 10/100'''

def main():
  a = 1
  b = 1
  x = 0
  y = 0
  
  for y in range (1,11):
    if(a%2 == 0):
      y = a*a
      x -= b/y
      a += 1
      b += 1
    else:
      y = a*a
      x += b/y
      a += 1
      b += 1

  print(x)
  return 0

if __name__ == "__main__":
  main()