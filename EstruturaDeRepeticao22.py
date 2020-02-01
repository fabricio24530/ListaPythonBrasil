'''Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
divisível.'''

number = int(input('Enter a integer number: '))
list_ = list()
divisible_list = list()
not_divisible_list = list()
cont_np = 0
cont_yp = 0

for i in range(number):
    list_.append(i)

for i in list_:
    if number % (i+1) == 0:
        cont_yp += 1
        divisible_list.append(i + 1)

if cont_yp == 2:
    print(f'The number {number} is prime')
    print(f'The number is divisible by {divisible_list}')
elif cont_yp > 2:
    print(f'The number {number} is not prime.')
    print(f'The number is divisible by {divisible_list}')
