'''Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
'''

termos = int(input('Informe a quantidade de termos: '))

numerador = 1
denominador = 2
lista = [1]
print('H = 1 +', end='')
for i in range(termos - 1):
    if i != termos - 2:
        print(f' {numerador}/{denominador}', end=' +')
    else:
        print(f' {numerador}/{denominador}')
    denominador += 1
    lista.append(numerador/denominador)

soma = sum(lista)

print(f'H = {soma:.2f}')