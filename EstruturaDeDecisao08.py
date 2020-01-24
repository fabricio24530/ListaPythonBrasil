'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato.'''

lista = list()

for i  in range(3):
    produto = float(input(f'Informe o preço do {i + 1}º produto: '))
    lista.append(produto)
menor = min(lista)
posicao = lista.index(menor)

print(f'O {posicao + 1}º produto possui o menor preço: R$ {menor}')
