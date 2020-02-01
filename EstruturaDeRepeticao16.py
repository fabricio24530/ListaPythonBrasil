'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que
o valor seja maior que 500.'''

n1 = 1
n2 = 1
n = 0
print(n1, n2, end=' ')
while n < 500:
    n = n1 + n2
    print(n, end=' ')
    n1 = n2
    n2 = n
