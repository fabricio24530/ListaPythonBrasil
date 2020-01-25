'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;'''

lados = list()

for i in range(3):
    lado = float(input(f'Informe o {i + 1}° lado: '))
    lados.append(lado)

if (abs(lados[1] - lados[2]) < lados[0] < lados[1] + lados[2]) and (abs(lados[0] - lados[2]) < lados[1] < lados[0] + lados[2]) and (abs(lados[0] - lados[1]) < lados[2] < lados[0] + lados[1]):
    print(f'O lados {lados[0]}, {lados[1]} e {lados[2]} formam um triangulo.')
    if lados[0] == lados[1] and lados[1] == lados[2]:
        print('Triangulo Equilátero.')
    elif (lados[0] == lados[1] and lados[1] != lados[2]) or (lados[0] == lados[1] and lados[1] != lados[2]) or (lados[1] == lados[2] and lados[2] != lados[0]):
        print('Triangulo Isósceles')
    else:
        print('Triangulo Escaleno')
else:
    print(f'O lados {lados[0]}, {lados[1]} e {lados[2]} não formam um triangulo.')
