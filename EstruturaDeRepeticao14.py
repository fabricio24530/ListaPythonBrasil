'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
números impares.'''

cont_par = 0
cont_impar = 0

for i in range(10):
    num = int(input(f'Informe o {i + 1}º numero: '))
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(f'''Pares: {cont_par}
Impares: {cont_impar}''')