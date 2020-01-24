'''Faça um Programa que leia três números e mostre o maior deles.'''

lista = list()

for i in range(3):
    num = float(input(f'Informe o {i + 1}° número: '))
    lista.append(num)

print(f'O maior numero digitado foi {max(lista)}')
