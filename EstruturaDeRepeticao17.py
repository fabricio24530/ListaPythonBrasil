'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''

num = int(input('Informe um numero inteiro: '))
fatorial = num

print(f'{num}! = ', end=' ')

for i in range(num):

    if num != 1:
        print(f'{num} x', end=' ')
    else:
        print(f'{num} = ', end=' ')
    num = num - 1
    if num != 0:
        fatorial = fatorial * num
    else:
        pass

print(f'{fatorial}')

