'''Faça um programa que calcule o mostre a média aritmética de N notas.'''

n = int(input('Quantidade de notas: '))
lista = list()

for i in range(n):
    nota = float(input(f'Informe a {i + 1}º nota: '))
    lista.append(nota)

media = sum(lista) / len(lista)

print()
print(f'A media das notas foi de {media:.1f}')

