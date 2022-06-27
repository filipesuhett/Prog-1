'''Faça um programa que verifique os números de 1 a 5000 (ambos incluídos), identificando os que são quadrados perfeitos e capicuas (capicuas é aquilo que lido de trás para frente é a mesma coisa: 121, 1001, 4334 etc)

Utilize as seguintes funções externas criadas por você:

a) uma função que retorne o tamanho de um número 

b) um função que inverta um número

c) uma função que verifique se o número é um quadrado perfeito

d) um função que verifique se um número é uma capicua

os outputs devem seguir o seguinte modelo

X É CAPICUA E QUADRADO PERFEITO

OU

X É CAPICUA

OU

X É QUADRADO PERFEITO

onde X é o número que está sendo testado'''

def f_inverte(n):
  x = 0
  p = f_tam(n)-1
  while (n > 0):
    resto = n % 10
    x += resto*10**p
    p = p - 1
    n = n // 10
     
  return x

def f_tam(n):
 cont = 0
 while (n > 0):
   n = n // 10
   cont += 1
 return cont


def f_qp(n):
   metade = n // 2 + 1
   divisor = 1
   if (n == 1):
     return True
   while (divisor < metade):
    if (divisor ** 2 == n):
     return True 
    divisor += 1
   return False
 
def f_ehCapicua(n):
    if (n == f_inverte(n) and n > 9):
     return True
    else:
     return False

 
def main():
 for n in range(1,5001):
   if (f_qp(n) and f_ehCapicua(n)):
     print(f'{n} É CAPICUA E QUADRADO PERFEITO')
   elif (f_ehCapicua(n)):
     print(f'{n} É CAPICUA')
   elif (f_qp(n)):
     print(f'{n} É QUADRADO PERFEITO')
 
 

 
if __name__ == "__main__":
 main()