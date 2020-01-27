'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

nome = input('Informe seu nome: ').strip().lower()
idade = int(input('Informe sua idade: '))
salario = float(input('Informe seu salario R$: '))
sexo = input('''Informe seu sexo: 
[F] - Femenino 
[M] - Masculino
''').strip().lower()
estado_civil = input('''Informe seu estado civil: 
[S] - Solteiro(a)
[C] - Casado(a)
[V] - Viuvo(a)
[D] - Divorciado(a)
''').strip().lower()

lista = ('s', 'c', 'v', 'd')

while True:
    if len(nome) > 3 and 0 < idade <= 150 and salario > 0 and (sexo == 'f' or sexo == 'm') and estado_civil in lista:
        break
    else:
        print('Valores invalidos!!!Repita!!!')
        print()
        nome = input('Informe seu nome: ').strip().lower()
        idade = int(input('Informe sua idade: '))
        salario = float(input('Informe seu salario R$: '))
        sexo = input('''Informe seu sexo: 
        [F] - Femenino 
        [M] - Masculino
        ''').strip().lower()
        estado_civil = input('''Informe seu estado civil: 
        [S] - Solteiro(a)
        [C] - Casado(a)
        [V] - Viuvo(a)
        [D] - Divorciado(a)
        ''').strip().lower()