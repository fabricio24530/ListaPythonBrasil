'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

def soma(a: float, b: float):
    return a + b
def subtracao(a: float, b:float):
    return a - b
def multiplicacao(a: float, b: float):
    return  a * b
def divisao(a: float, b: float):
    return a / b

numeros = list()

for i in range(2):
    n = float(input(f'Informe o {i+1}º numero: '))
    numeros.append(n)

operacao = input('''Informe a operação desejada: 
[S] - Soma
[SU] - Subtração
[M] - Multiplicação
[D] - Divisão
''').strip().lower()

if operacao == 's':
    valor = soma(numeros[0], numeros[1])
elif operacao == 'su':
    valor = subtracao(numeros[0], numeros[1])
elif operacao == 'm':
    valor = multiplicacao(numeros[0], numeros[1])
elif operacao == 'd':
    valor = divisao(numeros[0], numeros[1])
if valor == 0:
    par_impar = 'Nulo'
elif valor % 2 == 0:
    par_impar = 'Par'
else:
    par_impar = 'Impar'
if valor == 0:
    positivo_negativo = 'Nulo'
elif valor > 0:
    positivo_negativo = 'Positivo'
else:
    positivo_negativo = 'Negativo'
if '.' in str(valor) and '.0' not in str(valor):
    inteiro_decimal = 'Decimal'
else:
    inteiro_decimal = 'Inteiro'

print(f'{valor:.2f} é: {par_impar}, {positivo_negativo} e {inteiro_decimal}')

