'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.'''

int_1 = int(input('Informe um numero inteiro: '))
int_2 = int(input('Informe um numero inteiro: '))
float_1 = float(input('Informe um numero real: '))

a =  (int_1 ** 2) * (int_2 / 2)
b =  (int_1 ** 3) + float_1
c = pow(float_1, 3)

print(f'{a}, {b}, {c:.2f}')
