'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
  que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''
  
from math import ceil

area_a_ser_pitanda = float(input('Informe a area a ser pitada em m²: '))

total_de_litros = area_a_ser_pitanda / 3
total_de_latas = ceil(total_de_litros / 18)
valor_total = total_de_latas * 80

print(f'''Quantidade de latas: {total_de_latas}''')
print(f'Valor total: R$ {valor_total}')



