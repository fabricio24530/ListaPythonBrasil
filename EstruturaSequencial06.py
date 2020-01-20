'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''
from math import  pi

raio = float(input('Informe o raio do circulo: '))

area = pi * pow(raio, 2)

print(f'A area do circulo de raio {raio}u é {area:.2f}u²')
