'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que
é divisível somente por ele mesmo e por 1.'''

number = int(input('Enter a integer number: '))
list_ = list()
cont_yp = 0

for i in range(number):
    list_.append(i)

for i in list_:
    if number % (i+1) == 0:
        cont_yp += 1

if cont_yp == 2:
    print(f'The number {number} is prime')
else:
    print(f'The number {number} is not prime.')
