'''Deseja-se fazer uma pesquisa a respeito do consumo mensal de energia elétrica em
uma determinada cidade. Para isso, são fornecidos os seguintes dados:
- preço do kWh consumido;
- número do consumidor;
- quantidade de kWh consumidos durante o mês;
- código do tipo de consumidor (R-residencial, C-comercial, I-industrial).
O número do consumidor igual a zero deve ser usado como flag de parada. Fazer um algoritmo que:
- leia os dados descritos acima:
- calcule:
a) para cada consumidor, o total a pagar;
b) o maior consumo verificado;
c) o menor consumo verificado;
d) o total do consumo para cada um dos três tipos de consumidores;
e) a média geral de consumo;'''

def main():
  valor = float(input())
  numc = int(input())
  conm = 0
  com = 1000
  totalr = 0
  totalc = 0
  totali = 0
  cont = 0
  soma = 0
  medi = 0
  
  while (numc != 0):
    quantk = int(input())
    rcd = input().upper()

    total = valor*quantk

    cont += 1
    soma += quantk
    medi = soma/cont

    if(conm < quantk):
      conm = quantk
    if(com > quantk and quantk != 0):
      com = quantk
    
    if(rcd == "R"):
      totalr += quantk
    elif(rcd == "C"):
      totalc += quantk
    elif(rcd == "I"):
      totali += quantk
    
    print(numc, total)

    numc = int(input())

  print(conm)
  print(com)
  print(totalr)
  print(totalc)
  print(totali)
  print(medi)
  
  return 0
if __name__ == "__main__":
  main()