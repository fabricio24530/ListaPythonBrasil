'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa
deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o
funcionamento, o estilo e o número de testes (divisões) executados.'''

n = int(input('Informe o final do intervalo: '))

lista_numeros = list(range(1, (n+1)))
lista = list()
lista_primos = list()

for i in lista_numeros[::-1]:
    for j in lista_numeros:
        if i % j == 0:
            lista.append(i)

for i in lista:
    if lista.count(i) == 2:
        lista_primos.append(i)

lista_primos.append(1)  # Incluir sempre o 1
lista_primos = list(set(lista_primos))  # Função set tira valores duplicados na lista

print(f'Os numeros primos entre 1 e {n} são:', end=' ')
for i in lista_primos:
      print(i, end=' ')

print(f'\nE a quantidade de divisoes feitas foram de {sum(lista_primos)}')

















