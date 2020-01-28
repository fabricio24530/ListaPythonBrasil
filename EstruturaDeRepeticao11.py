'''Altere o programa anterior(EstruturaDeRepeticao10.py) para mostrar no final a soma dos números.'''

inicio_intervalo = int(input('Informe o inicio do intervalo: '))
final_intervalo = int(input('Informe o final do intervalo: '))
lista = list()

for i in range(inicio_intervalo, final_intervalo + 1):
    lista.append(i)

print(sum(lista))