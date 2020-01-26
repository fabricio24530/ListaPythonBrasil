'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno
e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.'''

notas = list()

for i in range(3):
    n = float(input(f'Informe a {i+1}º nota: '))
    notas.append(n)

media = sum(notas) / len(notas)

if 7 <= media < 10:
    print(f'Aprovado: media {media:.2f}')
elif media < 7:
    print(f'Reprovado: media {media:.2f}')
elif media == 10:
    print(f'Aprovado com distinção: media {media}')
    
