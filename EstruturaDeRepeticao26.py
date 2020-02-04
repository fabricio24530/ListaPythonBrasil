'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
votar e ao final mostrar o número de votos de cada candidato.
'''

eleitores = int(input('Total de eleitores: '))
votos1, votos2, votos3 = 0, 0, 0


for i in range(eleitores):
    candidato = input('Informe em qual candidato quer votar: 1, 2 ou 3 ').strip()
    if candidato.isdecimal():
        if candidato == '1':
            votos1 += 1
        elif candidato == '2':
            votos2 += 1
        elif candidato == '3':
            votos3 += 1
    else:
        print('Valor errado')

print(f'Total de votos do candidato 1: {votos1}')
print(f'Total de votos do candidato 2: {votos2}')
print(f'Total de votos do candidato 3: {votos3}')
