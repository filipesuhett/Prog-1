'''Jogo de Craps.

Faça um programa de implemente um jogo de Craps.

O jogador lança um par de dados, obtendo um valor entre 2 e 12.

Se, na primeira jogada, você tirar 7 ou 11, é um "natural" e você ganhou.

Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.

Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto".

Seu objetivo agora é continuar jogando os dados até tirar este número outra vez, quando você tirar esse número, você "ganhou". Apresente o número de jogadas que foram necessárias para você ganhar.

No entanto, você perde, se tirar um 7 antes de tirar este "Ponto" novamente. Apresente o número de jogadas que você fez até perder.'''

def main():
  y = int(input(""))
  joga = 1
  x = 10
  print(y)
  
  if(y==7 or y==11):
    print(f'{y} \nNATURAL! VOCÊ GANHOU \nJOGADAS = 1 ')
  elif(y==2 or y==3 or y==12):
    print(f'{y} \nCRAPS! VOCÊ PERDEU \nJOGADAS = 1 ')
  else:
    while(x == 10):
      joga += 1
      z = int(input(""))
      print(z)
      
      if(z == y):
        x += 10
        print("VOCÊ GANHOU")
        
      elif(z == 7):
        x += 10
        print("VOCÊ PERDEU")

    print(f'JOGADAS = {joga}')
      
  return 0

if __name__ == "__main__":
  main()