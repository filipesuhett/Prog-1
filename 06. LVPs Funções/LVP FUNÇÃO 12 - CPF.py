'''Faça um programa que, dados os nove primeiros números e os dois dígitos verificadores, informe se o CPF é válido ou inválido.

A regra de negócio (validação)  deve ser feita em formato de função.

Algoritmo do CPF - O que está por trás do gerador de CPF

Para exemplificar o processo vamos gerar um CPF válido, calculando os dígitos verificadores de um número hipotético, 111.444.777-XX.

Calculando o Primeiro Dígito Verificador

O primeiro dígito verificador do CPF é calculado utilizando-se o seguinte algoritmo. 

1) Distribua os 9 primeiros dígitos em um quadro colocando os pesos 10, 9, 8, 7, 6, 5, 4, 3, 2 abaixo da esquerda para a direita, conforme representação abaixo:

1	1	1	4	4	4	7	7	7
10	9	8	7	6	5	4	3	2
2) Multiplique os valores de cada coluna:

1	1	1	4	4	4	7	7	7
10	9	8	7	6	5	4	3	2
10	9	8	28	24	20	28	21	14
3) Calcule o somatório dos resultados (10+9+...+21+14) = 162

4) O resultado obtido (162) será divido por 11. Considere como quociente apenas o valor inteiro, o resto da divisão será responsável pelo cálculo do primeiro dígito verificador.

Vamos acompanhar: 162 dividido por 11 obtemos 14 como quociente e 8 como resto da divisão. Caso o resto da divisão seja menor que 2, o nosso primeiro dígito verificador se torna 0 (zero), caso contrário subtrai-se o valor obtido de 11, que é nosso caso. Sendo assim nosso dígito verificador é 11-8, ou seja, 3 (três). Já temos portanto parte do CPF, confira: 111.444.777-3X.

Calculando o Segundo Dígito Verificador

1) Para o cálculo do segundo dígito será usado o primeiro dígito verificador já calculado. Montaremos uma tabela semelhante a anterior só que desta vez usaremos na segunda linha os valores 11,10,9,8,7,6,5,4,3,2 já que estamos incorporando mais um algarismo para esse cálculo. Veja:

1	1	1	4	4	4	7	7	7	3
11	10	9	8	7	6	5	4	3	2
2) Na próxima etapa faremos como na situação do cálculo do primeiro dígito verificador, multiplicaremos os valores de cada coluna e efetuaremos o somatório dos resultados obtidos: (11+10+...+21+6) = 204.

1	1	1	4	4	4	7	7	7	3
11	10	9	8	7	6	5	4	3	2
11	10	9	32	28	24	35	28	21	6
3) Realizamos novamente o cálculo do módulo 11. Dividimos o total do somatório por 11 e consideramos o resto da divisão.

Vamos acompanhar: 204 dividido por 11 obtemos 18 como quociente e 6 como resto da divisão.

4) Caso o valor do resto da divisão seja menor que 2, esse valor passa automaticamente a ser zero, caso contrário (como no nosso caso) é necessário subtrair o valor obtido de 11 para se obter o dígito verificador. Logo, 11-6= 5, que é o nosso segundo dígito verificador.

Neste caso chegamos ao final dos cálculos e descobrimos que os dígitos verificadores do nosso CPF hipotético são os números 3 e 5, portanto o CPF ficaria assim: 111.444.777-35.'''

def main():
  a = (input("a: "))
  a1 = int(a[0])
  a2 = int(a[1])
  a3 = int(a[2])
  a4 = int(a[4])
  a5 = int(a[5])
  a6 = int(a[6])
  a7 = int(a[8])
  a8 = int(a[9])
  a9 = int(a[10])
  a10 = (a[12:14])
  
  b1 = 10*a1
  b2 = 9*a2
  b3 = 8*a3
  b4 = 7*a4
  b5 = 6*a5
  b6 = 5*a6
  b7 = 4*a7
  b8 = 3*a8
  b9 = 2*a9
  t1 = b1+b2+b3+b4+b5+b6+b7+b8+b9
  t3 = t1%11
  t4 = 11-t3
  if(t3<2):
    t4 = 0
  else:
    t4 = t4
  
  p1 = 11*a1
  p2 = 10*a2
  p3 = 9*a3
  p4 = 8*a4
  p5 = 7*a5
  p6 = 6*a6
  p7 = 5*a7
  p8 = 4*a8
  p9 = 3*a9
  p10 = 2*t4
  g1 = p1+p2+p3+p4+p5+p6+p7+p8+p9+p10
  g3 = g1%11
  g4 = 11-g3
  if(g3<2):
    g4 = 0
  else:
    g4 = g4

  t4 = str(t4)
  g4 = str(g4)
  s = t4+g4

  if(s==a10):
    print("CPF VÁLIDO")
  else:
    print("CPF INVÁLIDO")
  return 0

if __name__ == "__main__":
  main()