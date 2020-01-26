'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''

num = int(input('Informe um numero real menor que 1000: '))

c = num // 100
d = (num % 100) // 10
u = (num % 100) % 10

centena = 'centena'
dezena = 'dezena'
unidade = 'unidade'

if c >= 2 and d >= 2 and u >= 2 :
    centena, dezena, unidade = 'centenas', 'dezenas', 'unidades'
elif c >= 2 and d < 2 and u < 2:
    centena = 'centenas'
elif c >= 2 and d >= 2 and u < 2:
    centena, dezena = 'centenas', 'dezenas'
elif c >= 2 and d < 2 and u >= 2:
    centena, unidade = 'centenas', 'unidades'
elif c < 2 and d >= 2 and u < 2:
    dezena = 'dezenas'
elif c < 2 and d < 2 and u >= 2:
    unidade = 'unidades'
elif c < 2 and d >= 2 and u >= 2:
    dezena, unidade = 'dezenas', 'unidades'

if 0 <= num < 1000:
    print(f'{c} {centena}, {d} {dezena} e {u} {unidade}')


