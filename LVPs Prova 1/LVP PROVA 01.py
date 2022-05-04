#Faça um programa que leia um valor inteiro com três casas decimais e, utilizando recursos que já aprendemos em sala de aula, inverta esse número, entregando um valor inteiro de três casas decimais (PROIBIDO UTILIZAR QUALQUER RECURSO DE STRING). Ao final, o programa deverá verificar se o valor digitado é um PALÍNDROMO.

def main():
	 
  a = int(input("Numero:"))
	
  x = a%10
  y = (a%100)//10
  z = a//100
  b = x*100+y*10+z

  if (b==a):
    print(a, "É UM PALÍNDROMO")
  else:
    print(a, "NÃO É UM PALÍNDROMO")
  return 0

if __name__ == '__main__':
  main()