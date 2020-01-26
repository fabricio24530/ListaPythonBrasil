'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.'''

saque = float(input('Informe o valor a ser sacado: '))

if 10 <= saque <= 600:

    cem = saque // 100
    ciquenta = (saque % 100) // 50
    dez = ((saque % 100) % 50) // 10
    cinco = (((saque % 100) % 50) % 10) // 5
    um = ((((saque % 100) % 50) % 10) % 5)

    print(f'{cem} notas de R$ 100, {ciquenta} notas de R$ 50, {dez} notas de R$ 10, {cinco} notas de R$ 5 e {um} notas de R$ 1')
else:
    print('Saque nao permitido!!!')
    
