'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

lista = list()

for i in range(3):
    num = float(input(f'Informe o {i + 1}° número: '))
    lista.append(num)

print(f'O maior numero digitado foi {max(lista)}')
print(f'O menor numero digitado foi {min(lista)}')
