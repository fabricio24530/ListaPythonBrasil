'''Altere o programa anterior(EstruturaDeRepeticao04.py) permitindo ao usuário informar as populações e as taxas de
crescimento iniciais. Valide a entrada e permita repetir a operação.'''

contador = 0
sair = 0

while sair == 0:

    habitantes_pais_a = int(input('Informe a população inicial do pais com menor população: '))
    taxa_a = float(input('Informe a taxa de crescimento do pais com a menor população: '))
    habitantes_pais_b = int(input('Informe a população inicial do pais com maior população: '))
    taxa_b = float(input('Informe a taxa de crescimento do pais com a maior população: '))

    while habitantes_pais_b > habitantes_pais_a:

        habitantes_pais_a = habitantes_pais_a + (habitantes_pais_a * (taxa_a/100))
        habitantes_pais_b = habitantes_pais_b + (habitantes_pais_a * (taxa_b/100))
        contador += 1

    print(f'Em {contador} anos os paises terão a mesma quantidade populacional')

    sair = int(input('''Deseja repetir: 
    [0] - Sim 
    [1] - Não 
    '''))