'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal.'''

num = input('Informe um numero: ')

if '.' in num or ',' in num:
    print(f'{num} é decimal')
else:
    print(f'{num} é inteiro')
