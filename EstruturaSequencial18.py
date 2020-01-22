'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamanho_do_arquivo = float(input('Informe o tamanho do arquivo em MB: '))
velocidade_de_download = int(input('Informe a velocidade do download em Mbps: '))

tamanho_em_bytes = tamanho_do_arquivo
velocidade_em_bits = velocidade_de_download / 8
tempo = (tamanho_em_bytes / velocidade_em_bits) / 60


print(f'O tempo de Download sera de aproximadamente {tempo:.2f} minutos')
