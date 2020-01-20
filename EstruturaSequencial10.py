'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.'''

temp_c = float(input('Informe a temperatura em graus celsius: '))
temp_f = (9 * temp_c + 160) / 5

print(f'A temperatura {temp_c}°C equivale a {temp_f:2.f}°F')
