'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de  combustível (codificado da seguinte
forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

combustivel = input('''[A] - Alcool
[G] - Gasolina
 ''').strip().lower()
 
litros = float(input('Quantidade de litros: '))

if combustivel == 'g' and litros <= 20:
    valor = 2.5 * litros
    desconto = valor * 0.04
    total = valor - desconto
    print(f'Valor a ser pago: R$ {total:.2f}')
elif combustivel == 'g' and litros > 20:
    valor = 2.5 * litros
    desconto = valor * 0.06
    total = valor - desconto
    print(f'Valor a ser pago: R$ {total:.2f}')
elif combustivel == 'a' and litros <= 20:
    valor = 1.9 * litros
    desconto = valor * 0.03
    total = valor - desconto
    print(f'Valor a ser pago: R$ {total:.2f}')
elif combustivel == 'a' and litros <= 20:
    valor = 1.9 * litros
    desconto = valor * 0.05
    total = valor - desconto
    print(f'Valor a ser pago: R$ {total:.2f}')

