'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

lista = list()

for i in range(2):
    nota = float(input(f'Informe a {i + 1} nota: '))
    lista.append(nota)
media = sum(lista)/len(lista)

if  7 <= media < 10:
    print(f'A media do aluno foi de {media}: Aprovado')
elif media < 7:
    print(f'A media do aluno foi de {media}: Reprovado')
elif media == 10:
    print(f'Aprovado com distinção')

