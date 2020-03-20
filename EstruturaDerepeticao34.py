'''Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele
que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo.'''

num = int(input('Informe um numero: '))
lista1 = []

for i in range(num, 0, -1):
    if num % i == 0:
        lista1.append(i)

if len(lista1) == 2:
    print(f'O numero {num} é primo')
else:
    print(f'O numero {num} não é primo.')
