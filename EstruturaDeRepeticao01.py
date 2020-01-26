'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.'''

while True:  # Esta estrutura emula um 'do while' em Python
    num = int(input('Informe um valor de 0 a 10: '))
    if 0 <= num <= 10:
        print(num)
        break
    else:
        print('Valor invalido!!')
