'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.'''

ano = int(input('Informe um ano qualquer: '))

if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:  # Condição para um ano ser bissexto.
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
