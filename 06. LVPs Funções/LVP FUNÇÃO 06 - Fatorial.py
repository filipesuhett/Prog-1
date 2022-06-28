'''1) Faça um programa em Python3, DE FORMA MODULAR (DEFININDO E USANDO SUAS PRÓPRIAS FUNÇÕES), para resolver o seguinte problema:

a) Definir uma função em Python 3 que calcule o valor do fatorial de um número N inteiro maior ou igual a zero. Esta função recebe como parâmetro o valor de N. Esta função retorna o valor do fatorial de N calculado.

b) Faça um programa principal que leia diversos números inteiros maiores ou iguais a zero. Para cada número N lido imprima uma saída EXATAMENTE conforme o modelo apresentado nos casos de teste abaixo. A condição de parada da entrada de dados é ler um número N menor que zero.

c) Invocar o programa principal.

Modelo de solução a ser seguido:

# Função de cálculo da fatorial de N>0

def f_fatorial(n):

 .

  return fatorial

#fim da função

# função com o programa principal

def main():

  .

#fim da função main

#invocação/chamada do programa principal

if __name__ == "__main__":

  main()

#fim

Seu formato de saída deve ser IDÊNTICO A ESTE EXEMPLO, onde os valores de  N e de Fatorial(N) devem ser impressos com 0 casas decimais exatamente. Exemplo para N=0

Fatorial(0)=1'''

def f_factorial(a1=1):
  a = 1
  for b in range(a1,0,-1):
    a*= b
  return a



def main():
    a1 = int(input())

    while a1 >= 0:
        fac = f_factorial(a1)
        print(f'Fatorial({a1})={fac}')
        a1 = int(input())




if __name__=="__main__":
  main()