'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações.'''


while True:
    nome = input('Informe o nome de usuario: ').strip().lower()
    senha = input('Informe uma senha: ').strip().lower()
    if nome != senha:
        print('Usuario e senha cadastrados com sucesso')
        break
    else:
        print('Usuario e senha não podem ser iguais!!! Repita o processo!!!')
