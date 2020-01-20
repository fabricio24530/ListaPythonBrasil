'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.'''

valor_hora = float(input('Informe o valor da hora trabalhada R$: '))
qtd_horas_mes = float(input('Inform o valor da quantidade de horas trabalhadas no mÊs: '))

total_a_receber = valor_hora * qtd_horas_mes

print(f'''Neste mês você trabalho {qtd_horas_mes}h, logo o total a receber, tendo como base o valor da hora trabalhada, 
é de R${total_a_receber:.2f}''')
