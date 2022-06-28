'''Regras para o ano BISSEXTO

- Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;

- Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;

- Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.

Desafio Padawan: Fazer o código da FUNÇÃO em apenas uma linha de return'''

def f_bissexto(a):
  return (a%4==0 and a%100!=0) or (a%400==0)

def main():
  a = int(input("Escreva o ano aqui: "))
  if (f_bissexto(a)):
    print("É BISSEXTO")
  else:
    print("NÃO É BISSEXTO")
  return 0

if __name__ == "__main__":
  main()