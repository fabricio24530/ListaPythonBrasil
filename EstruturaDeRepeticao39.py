'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
alto e o número do aluno mais baixo, junto com suas alturas.'''

dicionario = {}
lista_altura = []
lista_nome = []

for i in range(3):
    nome = input('Numero do aluno: ')
    altura_aluno = float(input('Altura do aluno: '))
    dicionario[nome] = altura_aluno

for i in dicionario.values():
    lista_altura.append(i)

for j in dicionario.keys():
    lista_nome.append(j)

aluno_mais_alto = lista_nome[lista_altura.index(max(lista_altura))]
maior_altura = max(lista_altura)
aluno_mais_baixo = lista_nome[lista_altura.index(min(lista_altura))]
menor_altura = min(lista_altura)

print(f'Aluno mais alto: {aluno_mais_alto} com {maior_altura:.2f}m')
print(f'Aluno mais baixo: {aluno_mais_baixo} com {menor_altura:.2f}m')


