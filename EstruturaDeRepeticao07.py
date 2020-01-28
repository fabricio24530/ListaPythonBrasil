'''Faça um programa que leia 5 números e informe o maior número.'''

lista = list()

for i in range(5):
    num = float(input(f'Informe o {i+1}º numero: '))
    lista.append(num)

print(f'O maior valor digitado foi: {max(lista)}')