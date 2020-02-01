'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.'''

lista = list()
qtd = int(input('Quantidade de numeros do conjunto: '))

for i in range(qtd):
    numero = int(input(f'Informe o {i+1}º numero: '))
    lista.append(numero)

print(f'''Menor valor digitado: {min(lista)}
Maior valor digitado: {max(lista)}
Soma dos valores: {sum(lista)}''')