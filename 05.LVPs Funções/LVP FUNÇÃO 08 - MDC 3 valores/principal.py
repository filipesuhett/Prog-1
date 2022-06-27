'''Baseado no exercício 1.12.60 Livro Farrer - página 85 com algumas modificações no enunciado.

Faça um programa em Python3, DE FORMA MODULAR (DEFININDO E USANDO SUAS PRÓPRIAS FUNÇÕES) EM ARQUIVO EXTERNO para resolver o seguinte problema:

a) Definir uma função em Python 3 que calcule o valor do máximo divisor comum (mdc) entre três números inteiros positivos. Esta função recebe como parâmetro três números inteiros positivos e retorna o valor do mdc calculado. 

b) Faça um programa principal que leia 4 conjuntos com 3 números inteiros positivos. Para cada conjunto de três números lidos, imprima os números lidos na ordem em que foram lidos e o valor do mdc calculado. A saída deste programa deverá ser EXATAMENTE conforme o modelo apresentado nos casos de teste abaixo.

c) Invocar o programa principal.

Seu formato de saída deve ser IDÊNTICO A ESTE EXEMPLO, onde os valores de  N1, N2 e N3 são os três números de entrada lidos, e RESULTADO é o valor resultante do cálculo do mdc entre N1, N2 e N3.'''

from secundaria import f_mult
def main():
  cont= 1
  while (cont <= 4):
    cont += 1  
    a = int(input())
    b = int(input())
    c = int(input())
    a1 = f_mult(a,b,c)
    print(f'MDC=({a},{b},{c}) = {a1}')

if __name__=="__main__":
  main()