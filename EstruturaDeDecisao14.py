'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

notas = list()
for i in range(2):
    nota = float(input(f'Informe a {i + 1}º nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

if 9 < media <= 10:
    print(f'''1º nota: {notas[0]}
2º nota: {notas[1]}
Media: {media:.2f}
Conceito: A
Situação: APROVADO''')

elif 7.5 < media <= 9:
    print(f'''1º nota: {notas[0]}
2º nota: {notas[1]}
Media: {media:.2f}
Conceito: B
Situação: APROVADO''')

elif 6 < media <= 7.5:
    print(f'''1º nota: {notas[0]}
2º nota: {notas[1]}
Media: {media:.2f}
Conceito: C
Situação: APROVADO''')

elif 4 < media <= 6:
    print(f'''1º nota: {notas[0]}
2º nota: {notas[1]}
Media: {media:.2f}
Conceito: D
Situação: REPROVADO''')

elif 0 <= media <= 4:
    print(f'''1º nota: {notas[0]}
2º nota: {notas[1]}
Media: {media:.2f}
Conceito: E
Situação: REPROVADO''')
