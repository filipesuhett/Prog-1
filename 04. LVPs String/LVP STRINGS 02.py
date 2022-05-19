'''Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas e, OBRIGATORIAMENTE, comando de repetição. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.'''

def main():
    y = input("").upper()
    
    print(y[::-1])
     

if __name__ == "__main__":
  main()