'''Altere o programa anterior - EstruturaDeRepeticao18 -  para que ele aceite apenas números entre 0 e 1000.'''

lista = list()
cont = 0
qtd = int(input('Quantidade de numeros do conjunto: '))
i = 1

while cont != qtd:

    numero = int(input(f'Informe o {i}º numero entre 0 e 1000: '))

    if 0 < numero < 1000:
        lista.append(numero)
        cont += 1
        i += 1
    else:
        print('Numero fora do intevalor!!!! Repita!!!!')

print(f'''Menor valor digitado: {min(lista)}
Maior valor digitado: {max(lista)}
Soma dos valores: {sum(lista)}''')
