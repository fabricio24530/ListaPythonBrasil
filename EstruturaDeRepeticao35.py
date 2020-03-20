'''Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre
1 e um número inteiro informado pelo usuário.'''

num = int(input('Informe um numero: '))
lista = []
lista2 = []

for i in range(num, 0, -1):
    for j in range(num, 0, -1):
        if i % j == 0:
            lista.append(i)

for k in lista:
    if lista.count(k) == 2 and k not in lista2:
        lista2.append(k)

print(f'O numeros primos entre 1 e {num} são: \n{lista2[::-1]}')



