'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''

lista_cidade = []
lista_veiculos = []
lista_acidentes = []
lista_acidentes2 = []

for i in range(5):
    cidade = int(input('Informe o codigo da cidade: '))
    lista_cidade.append(cidade)
    veiculos = int(input('Informe a quantidade de veiculos: '))
    lista_veiculos.append(veiculos)
    acidentes = int(input('Informe o numero de acidentes: '))
    lista_acidentes.append(acidentes)
    if veiculos <= 2000:
        lista_acidentes2.append(acidentes)

media_veiculos = sum(lista_veiculos)/len(lista_veiculos)
maior_qtd_acidentes = max(lista_acidentes)
menor_qtd_acidentes = min(lista_acidentes)
if len(lista_acidentes2) > 0:
    media_acidentes2 = sum(lista_acidentes2)/len(lista_acidentes2)

print(f'O maior numero de acidentes foi de {maior_qtd_acidentes} na cidade de codigo {lista_cidade[lista_acidentes.index(max(lista_acidentes))]}')
print(f'O menor numero de acidentes foi de {menor_qtd_acidentes} na cidade de codigo {lista_cidade[lista_acidentes.index(min(lista_acidentes))]}')
print(f'A media de veiculos das 5 cidades juntas é de {media_veiculos:.2f} veiculos')
print(f'A media de acidentes em cidades com menos de 2000 veiculos é de {media_acidentes2:.2f} acidentes')