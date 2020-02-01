'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a
série até o n−ésimo termo.'''

termo = int(input('Ate que termo deseja imprimir: '))

n1 = 1
n2 = 1

print(n1, n2, end=' ')
for i in range(termo - 2):  # Os dois primeiros termos são constantes.
    n = n1 + n2
    print(n, end=' ')
    n1 = n2
    n2 = n


