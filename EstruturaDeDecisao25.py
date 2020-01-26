'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

lista = list()

p1 = input('Telefonou para a vítima? [S] - Sim [N] - Não ').strip().lower()
lista.append(p1)
p2 = input('Esteve no local do crime? [S] - Sim [N] - Não ').strip().lower()
lista.append(p2)
p3 = input('Mora perto da vítima? [S] - Sim [N] - Não ').strip().lower()
lista.append(p3)
p4 = input('Devia para a vítima? [S] - Sim [N] - Não ').strip().lower()
lista.append(p4)
p5 = input('Já trabalhou com a vítima? [S] - Sim [N] - Não ').strip().lower()
lista.append(p5)
print()
print()

total_sim = lista.count('s')

if total_sim == 2:
    print('Supeita!')
elif total_sim == 4 or total_sim == 3:
    print('Cumplice!')
elif total_sim == 5:
    print('Culpada!')
else:
    print('Inocente!')


