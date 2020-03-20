'''Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário,
conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.'''

while True:

    tabuada_de = int(input('Tabuada de: '))
    comeco_tabuada = int(input('Começando por: '))
    fim_tabuada = int(input('Terminando por: '))
    print()
    print()

    if comeco_tabuada < fim_tabuada:

        print(f'Vou montar a tabuada de {tabuada_de} começando em {comeco_tabuada} e terminado em {fim_tabuada}:\n')

        for i in range(comeco_tabuada, fim_tabuada + 1):
            print(f'{tabuada_de} x {i} = {tabuada_de * i}')
        break
    else:
        print('O comeco da tabuada nao pode ser menor que o fim. REPITA!!!\n')