'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
- Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima,
 isto é, considere latas cheias.'''

from math import ceil

area_a_ser_pintada = float(input('Informa o tamanho em m² da area a ser pitada: '))

qtd_de_tinta = ceil(area_a_ser_pintada / 6) + (ceil(area_a_ser_pintada / 6) * 0.1)
qtd_de_latas_18 = qtd_de_tinta // 18
qtd_de_latas_3_6 = (qtd_de_tinta % 18) // 3.6
valor_tota_misto = (qtd_de_latas_18 * 80) + (qtd_de_latas_3_6 * 25)

print(f'''Quantidade de tinta:{qtd_de_tinta} l
Quantidade de latas de 18l: {int(qtd_de_latas_18)}
Quantidade de latas de 3.6l: {ceil(qtd_de_latas_3_6)}
Valor total: R$ {valor_tota_misto:.2f}''')


