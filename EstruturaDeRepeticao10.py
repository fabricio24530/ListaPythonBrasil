'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''
inicio_intervalo = int(input('Informe o inicio do intervalo: '))
final_intervalo = int(input('Informe o final do intervalo: '))

for i in range(inicio_intervalo, final_intervalo + 1):
    print(i)