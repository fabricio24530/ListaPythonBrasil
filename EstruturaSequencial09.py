'''Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).'''

temp_f = float(input('Informe a temperatura em graus Farenheit: '))
temp_c = (5 * (temp_f-32) / 9)
print(f'A temperatura {temp_f}°F equivale a {temp_c:.2f}°C')

