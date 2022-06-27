'''Faça um programa em linguagem Python que lê um número n digitado pelo usuário(esse número vai ser a quantidade de termos) e imprime os n primeiros números da sequência de Fibonacci.'''

def f_fibon(a):
  ult=0
  pen=1
  
  if (a==1) or (a==2):
      print("1")
  else:
    cont=1
    while cont <= a:
        ter = ult + pen
        pen = ult
        ult = ter
        cont += 1
        print(ter)

    
def main():
  a = int(input('Quantos termos serão somados? '))
  b = f_fibon(a)
  print(b)


if __name__=="__main__":
  main()