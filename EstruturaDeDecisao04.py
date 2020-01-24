'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

vogais = ['a', 'e', 'i', 'o', 'u']

entrada = input('Informe uma letra: ')

if entrada.strip().lower() in vogais:
    print(f'"{entrada.strip()}" é uma vogal.')
else:
    print(f'"{entrada.strip()}" é uma consoante.')
