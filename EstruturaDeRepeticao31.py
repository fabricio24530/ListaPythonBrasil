'''O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para e
ntão calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a
 próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00'''

cont = 1
soma = 0
lista = []

while True:

    produto = float(input('Valor do produto: '))
    if produto == 0:
        break
    else:
        lista.append(produto)

valor_total = sum(lista)
dinheiro = float(input('Valor dado pelo cliente: '))
troco = dinheiro - valor_total

for i in range(len(lista)):
    print(f'Produto {i+1}: R$ {lista[i]}')

print(f'Total: R$ {valor_total}\nDinheiro: R$ {dinheiro}\nTroco: R$ {troco}')
