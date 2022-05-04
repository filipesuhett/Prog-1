#Faça um programa que, dados 4 números inteiros com entrada, apresenta a soma do maior e do menor valor.
#OBS: Fiz de forma burra.

def main():
  a = int(input(""))
  b = int(input(""))
  c = int(input(""))
  d = int(input(""))

  if(a>b>c>d):
    print(a+d)
  elif(a>b>d>c):
    print(a+c)
  elif(a>c>d>b):
    print(a+b)
  elif(a>c>b>d):
    print(a+d)
  elif(a>d>b>c):
    print(a+c)
  elif(a>d>c>b):
    print(a+b)
  elif(b>a>c>d):
    print(b+d)
  elif(b>a>d>c):
    print(b+c)
  elif(b>c>a>d):
    print(b+d)
  elif(b>c>d>a):
    print(b+a)
  elif(b>d>a>c):
    print(b+c)
  elif(b>d>c>a):
    print(b+a)
  elif(c>a>b>d):
    print(c+d)
  elif(c>a>d>b):
    print(c+b)
  elif(c>b>d>a):
    print(c+a)
  elif(c>b>a>d):
    print(c+d)
  elif(c>d>a>b):
    print(c+b)
  elif(c>d>b>a):
    print(c+a)
  elif(d>a>b>c):
    print(d+c)
  elif(d>a>c>b):
    print(d+b)
  elif(d>b>a>c):
    print(d+c)
  elif(d>b>c>a):
    print(d+a)
  elif(d>c>a>b):
    print(d+b)
  else:
    print(d+a)

  return 0
if __name__ == "__main__":
  main()


#Jeito certo

def main():
    soma = 0
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if (a > b and a > c and a > d):
        soma += a
    elif (b > c and b > d):
        soma += b
    elif (c > d):
        soma += c
    else:
        soma += d
    
    if (a < b and a < c and a < d):
        soma += a
    elif (b < c and b < d):
        soma += b
    elif (c < d):
        soma += c
    else:
        soma += d
    print(soma)

    return 0

if __name__ == "__main__":
    main()
