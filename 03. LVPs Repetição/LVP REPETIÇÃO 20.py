'''Não faça entrada de dados interativa.

O padrão para os nomes dos códigos fontes se mantém.

Declare todas as variáveis que utilizar em seus programas e com letras em minúsculo.

Faça os comentários mínimos em seu código, tipo:

#Declaração de variáveis

#Inicialização de variáveis

#Entrada de dados

#Processamento

#Saída de dados

Exercício 1.12.7 Livro Farrer - página 76 com algumas modificações no enunciado.

Faça um programa em Python3 para resolver o seguinte problema:

Deseja-se fazer um levantamento a respeito da ausência de alunos à primeira prova de Programação de Computadores para as N turmas de existentes no Ifes. O valor de N é fornecido pelo usuário. O valor de N (quantidade de turmas) é o primeiro dado fornecido ao usuário.

Para cada uma das N turmas existentes é fornecido um conjunto de valores nesta ordem:

- a identificação da turma - tipo (string);

- a quantidade de alunos matriculados - tipo (int);

Os demais dados desta turma são:

- a matrícula de um aluno - tipo (string)

- a frequência do aluno - a letra A (ausente) ou a letra P (presente) - tipo (string)

Fazer um programa que:

- Para cada uma das N turmas (N diversas turmas), calcule a porcentagem de ausência dos alunos. Imprima a identificação da turma e a porcentagem, calculada, de ausência de alunos com duas casas decimais.

- Determine e imprima qual turma teve a (primeira) maior porcentagem de ausência. Imprima a turma e sua respectiva porcentagem com duas casas decimais.

- Determine e imprima qual turma teve a (primeira) menor porcentagem de ausência. Imprima a turma e sua respectiva porcentagem com duas casas decimais.

- Determine e imprima quantas turmas tiveram porcentagem de ausência superior a 20%.

Formato de saída, exemplo para o caso de teste que possui 4 turmas:

input=4

turmaA
5
matrA1
A
matrA2
P
matrA3
P
matrA4
P
matrA5
P
turmaB
4
matrB1
P
matrB2
P
matrB3
P
matrB4
P
turmaC
4
matrC1
P
matrC2
A
matrC3
P
matrC4
P
turmaD
5
matrD1
P
matrD2
P
matrD3
A
matrD4
P
matrD5
P

Seu formato de saída deve ser IDÊNTICO A ESTE'''

def main():
    countTA = 0
    countTB = 0
    countTC = 0
    countTD = 0
    aus = 0
    maior = 0
    menor = 500
    count20 = 0
    turmas = int(input())
    for c in range(turmas):
        countA = 0
        tipo = input()
        qntdalunos = int(input())
        for i in range(qntdalunos):
            matricula = input()
            frequencia = input()

            if (frequencia == 'A'):
                countA += 1
        aus = countA * 100 / qntdalunos

        if (aus < menor):
            menor = aus
            namemenor = tipo
        elif (aus > maior):
            maior = aus
            namemaior = tipo
        if (aus > 20):
            count20 += 1
        print(f'TURMA = {tipo} AUSENCIA = {aus:.2f} %')
    print(f'TURMA COM MAIOR % DE AUSENCIA= {namemaior} AUSENCIA= {maior:.2f}%')
    print(f'TURMA COM MENOR % DE AUSENCIA= {namemenor} AUSENCIA= {menor:.2f}%')

    print(f'{count20} TURMAS COM % DE AUSENCIA SUPERIOR A 20%')


if __name__ == "__main__":
    main()
