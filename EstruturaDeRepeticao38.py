'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o
usuário digite o salário inicial do funcionário.'''

ano = int(input('Informe o ano atual: '))
salario_inicial = float(input('Informe seu salario inicial: '))
total_anos = ano - 1996
novo_salario = 0
percentagem = 0.015

for i in range(1, total_anos + 1):
    percentagem *= 2
    print(percentagem)

