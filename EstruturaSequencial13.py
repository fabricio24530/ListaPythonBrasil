'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando
as seguintes fórmulas:
- Para homens: (72.7*h) - 58
- Para mulheres: (62.1*h) - 44.7'''

sexo = input('''Informe seu sexo:
[M] - Masculino
[F] - Femenino
''')

altura = float(input('Informe sua altura: '))

if sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
elif sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58

print(f'Seu peso ideal é de {peso_ideal:.2f}Kg')
