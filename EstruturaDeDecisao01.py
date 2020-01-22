'''Faça um Programa que peça dois números e imprima o maior deles'''
lista = list()

for i in range(2):
    n = int(input(f'Informe o {i + 1}° número: '))
    lista.append(n)

print(f'O maior numero digitado é {max(lista)}')
    
