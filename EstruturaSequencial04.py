'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

lista = []

for i in range(4):
    num = int(input(f'Informe o {i + 1}° numero: '))
    lista.append(num)
    
media = sum(lista)/4

print(f'A media foi  {media}')
