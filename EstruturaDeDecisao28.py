'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites
para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5%
sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um
cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do
desconto e valor a pagar.
'''

tipo_de_carne = input('''Informe o tipo de carne:
[F] - File duplo
[A] - Alcatra
[P] - Picanha
''').strip().lower()
print()

quantidade = float(input('Informe a quantidade de carne desejada em Kg: '))

pagamento = input('''Informe a forma de pagamento:
[C] - Cartão Tabajara
[O] - Outro
''').strip().lower()
print()

if tipo_de_carne == 'f' and quantidade <= 5 and pagamento == 'c':
    total_a_pagar = 4.5 * quantidade - (4.5*quantidade*0.1)
elif tipo_de_carne == 'f' and quantidade <= 5 and pagamento == 'o':
    total_a_pagar = 4.5 * quantidade
elif tipo_de_carne == 'f' and quantidade > 5 and pagamento == 'c':
    total_a_pagar = 5.8 * quantidade - (5.8*quantidade*0.1)
elif tipo_de_carne == 'f' and quantidade > 5 and pagamento == 'o':
    total_a_pagar = 5.8 * quantidade

if tipo_de_carne == 'a' and quantidade <= 5 and pagamento == 'c':
    total_a_pagar = 5.9 * quantidade - (5.9*quantidade*0.1)
elif tipo_de_carne == 'a' and quantidade <= 5 and pagamento == 'o':
    total_a_pagar = 5.9 * quantidade
elif tipo_de_carne == 'a' and quantidade > 5 and pagamento == 'c':
    total_a_pagar = 6.8 * quantidade - (6.8*quantidade*0.1)
elif tipo_de_carne == 'a' and quantidade > 5 and pagamento == 'o':
    total_a_pagar = 6.8 * quantidade

if tipo_de_carne == 'p' and quantidade <= 5 and pagamento == 'c':
    total_a_pagar = 6.9 * quantidade - (6.9*quantidade*0.1)
elif tipo_de_carne == 'p' and quantidade <= 5 and pagamento == 'o':
    total_a_pagar = 6.9 * quantidade
elif tipo_de_carne == 'p' and quantidade > 5 and pagamento == 'c':
    total_a_pagar = 7.8 * quantidade - (7.8*quantidade*0.1)
elif tipo_de_carne == 'p' and quantidade > 5 and pagamento == 'o':
    total_a_pagar = 7.8 * quantidade


if tipo_de_carne == 'f':
    print(f'''Tipo de carne : File duplo
Quantidade de carne : {quantidade} kg
Preço total : R$ {total_a_pagar:.2f}''')

elif tipo_de_carne == 'a':
    print(f'''Tipo de carne : Alcatra
Quantidade de carne : {quantidade} kg
Preço total : R$ {total_a_pagar:.2f}''')

elif tipo_de_carne == 'p':
    print(f'''Tipo de carne : Picanha
Quantidade de carne : {quantidade} kg
Preço total : R$ {total_a_pagar:.2f}''')

