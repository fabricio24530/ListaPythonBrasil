'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o
mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura
e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro,
além da média das alturas e dos pesos dos clientes'''

lista_codigo = list()
lista_peso = list()
lista_altura = list()


while True:

    cod = int(input('Insira o codigo do aluno: '))
    lista_codigo.append(cod)
    peso = float(input('Insira o peso do aluno: '))
    lista_peso.append(peso)
    altura = float(input('Insira a altura do aluno: '))
    lista_altura.append(altura)
    controle = input('Deseja inserir outro aluno:\n[S] - Sim\n[N] - Não\n').upper().strip()

    if controle == 'S':
        continue
    elif controle == 'N':
        break

maior_peso = max(lista_peso)
menor_peso = min(lista_peso)
peso_medio = sum(lista_peso)/len(lista_peso)

maior_altura = max(lista_altura)
menor_altura = min(lista_altura)
altura_media = sum(lista_altura)/len(lista_altura)

print(f'O aluno {lista_codigo[lista_peso.index(maior_peso)]} possui o maior peso: {maior_peso} kG')
print(f'O aluno {lista_codigo[lista_peso.index(menor_peso)]} possui o menor peso: {menor_peso} kG')
print(f'A media de peso entre os alunos é de: {peso_medio:.2f} kg')

print(f'O aluno {lista_codigo[lista_altura.index(maior_altura)]} possui a maior altura: {maior_altura} m')
print(f'O aluno {lista_codigo[lista_altura.index(menor_altura)]} possui a menor altura: {menor_altura} m')
print(f'A media das alturas entre os alunos é de: {altura_media:.2f} m')
