'''Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
calculada.'''

n = int(input('Quantas pessoas deseja verificar: '))
lista = list()

for i in range(n):
    idade = int(input(f'Informe a {i+1}º idade: '))
    lista.append(idade)

media = sum(lista)/len(lista)

if 0 < media < 25:
    print('Jovem')
elif 26 <= media < 60:
    print('Adulta')
elif media > 60:
    print('Idosa')