'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída d
eve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120'''

num = int(input('Informe um numero: '))
fatorial = 1

print(f'{num}! = ', end=' ')
for i in range(num, 0, -1):
    fatorial *= i
    if i != 1:
        print(f'{i} .', end=' ')
    else:
        print(f'{i} =', end=' ')

print(f'{fatorial}')
