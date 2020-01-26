'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

dia, mes, ano = input('Informe uma data no seguinte formato dd/mm/aaaa: ').split('/')

if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and  0000 <= int(ano) <= 9999 and len(dia) == 2 and len(mes) == 2 and len(ano) == 4:
    print(f'Formatato valido: {dia}/{mes}/{ano}')
else:
    print('Formato invalido!!!')

