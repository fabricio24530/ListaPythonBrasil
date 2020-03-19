'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas'''

quantidade = int(input('Informe a quantidade de temperaturas:'))
lista = []

for i in range(quantidade):
    temperatura = int(input(f'Inform a {i+1}º temperatura: '))
    lista.append(temperatura)

menor_temperatura = min(lista)
maior_temperatura = max(lista)
temperatura_media = sum(lista)/len(lista)

print(f'Maior temperatura: {maior_temperatura}° C\nMenor temperatura: {menor_temperatura}° C\nTemperatura media: {temperatura_media:.2f}° C')
