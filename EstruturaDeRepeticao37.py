'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o
mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura
e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro,
além da média das alturas e dos pesos dos clientes'''

var_controle = 1

dic_peso = {}
dic_altura = {}

while var_controle != 0:

    codigo = int(input('Informe seu codigo: '))


    peso = float(input('informe seu peso: '))
    altura = float(input('Informe sua altura: '))
    dic_peso[codigo] = peso
    dic_altura[codigo] = altura
    var_controle = int(input('Deseja cadastrar outro cliente:\n[1] - Sim\n[0] - Não\n'))

print(dic_peso)
print(dic_altura)


# print(f'O cliente mais pesado: {max(dic_peso)}')
# print(f'O cliente mais alto: {max(dic_altura)}')
