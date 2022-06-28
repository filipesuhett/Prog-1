'''Desenvolva um programa que receba, enquanto o usuário responder sim "s", dois valores para efetuar operações matemáticas de acordo com a opção do usuário, 1 para soma, 2 para subtração (do primeiro pelo segundo), 3 para multiplicação, 4 para divisão (do primeiro pelo segundo), 5 para exponenciação (o segundo número será a potência), 6 para  raiz (o primeiro número será o radicando e o segundo o índice). Qualquer valor diferente desse deve retornar uma mensagem de erro. Apresente o resultado da operação.'''

def main():
  y = input("").upper()
  c = 0
  
  while (y == "S"):
    a = int(input("a: "))
    b = int(input())
    c = int(input())
    y = input("").upper()

    if (a==1):
      print(b+c)
    elif (a==2):
      print(b-c)
    elif (a==3):
      print(b*c)
    elif (a==4):
      print(b/c)
    elif (a==5):
      print(b**c)
    elif (a==6):
      print(b**(1/c))
    else:
      print("OPERACAO INVALIDA")
  
  return 0
if __name__ == "__main__":
  main()