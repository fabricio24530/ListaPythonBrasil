'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
M - Masculino, Sexo Inválido.'''

sexo = input('''Digite:
[F] - Femenino
[M] - Masculino
''')

if sexo.lower() == 'f':
    print('F - Femenino')
elif sexo.lower() == 'm':
    print('M - Masculino')
else:
    print('Sexo invalido')
