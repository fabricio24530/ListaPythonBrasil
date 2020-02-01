'''Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
fatorial a números inteiros positivos e menores que 16.'''

exitt = 'y'

while exitt == 'y':

    num = int(input('Enter an integer, positive and less than 16: '))
    if 0 < num < 16:
        factorial = num

        print(f'{num}! = ', end=' ')

        for i in range(num - 1):
             num = num - 1
             factorial = factorial * num

        print(f'{factorial}')
        exitt = input('Do you wish calculater other factorial: [Y] - Yes [N] - No  ').strip().lower()
    else:
        print('Value error, REPEAT!!!')
