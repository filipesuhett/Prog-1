#Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

def main():

  a = float(input("a: "))            
  b = float(input("b: "))

  if (b<=1500):
    print(b*0.03+a)
  else:
    print((1500*0.03)+(b-1500)*0.05+a)
  
  return 0
if __name__ == "__main__":
  main()