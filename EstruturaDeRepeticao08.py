'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

lista = list()

for i in range(5):
    num = float(input(f'Informe o {i + 1}º numero: '))
    lista.append(num)

soma = sum(lista)
media = soma / len(lista)

print(f'''A soma dos valores é: {soma}
A media entre os valores é: {media:.2f}''')

