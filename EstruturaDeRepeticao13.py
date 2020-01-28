'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.'''

base = float(input('Informe a base: '))
expoente = int(input('Informe o expoente: '))
base1 = base
for i in range(expoente - 1):
    resultado = base1 * base  # A logica se resuma a esta linha!!!
    base1 = resultado

print(f'{base} elevado a {expoente} é igual a {resultado}')



