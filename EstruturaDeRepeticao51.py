'''Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. '''

n = int(input('Quantidade de termos: '))
de = 1
nu = 1
lista_soma = []

print('S =', end=' ')
for i in range(n):
    if i != n - 1:
        print(f'{de}/{nu} + ', end='')
    else:
        print(f'{de}/{nu}')
    lista_soma.append(de/nu)
    de += 1
    nu += 2
print(f'S = {sum(lista_soma):.2f}')