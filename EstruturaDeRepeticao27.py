'''Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.'''

qtd_turmar = int(input('Informe a quantidade de turmas: '))
lista = list()

for i in range(qtd_turmar):
    qtd_alunos = int(input(f'Informe a quantidade de alunos da {i + 1}º turma: '))
    lista.append(qtd_alunos)

media = sum(lista)/qtd_turmar

print(f'O numero medio de alunos por turma é de {media:.2f}')