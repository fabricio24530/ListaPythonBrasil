#!/usr/bin/python3
# -*- coding: utf-8 -*-


from timeit import default_timer as agora

final_intervalo = int(input('Informe o final do intervalo [1 a X]: '))
inicio_da_execucao_tudo = agora()

inicio_da_execucao_calculo = None
final_da_execucao_calculo = None

inicio_da_execucao_prints_dos_numeros = None
final_da_execucao_prints_dos_numeros = None


def calc_quant_primos(limite_intervalo):
    global inicio_da_execucao_calculo
    inicio_da_execucao_calculo = agora()

    quant_primos = 3
    primos_no_intervalo = {1: 2, 2: 3, 3: 5}
    for numero_analisado in range(7, limite_intervalo + 1, 2):
        if str(numero_analisado)[-1] == '5':
            continue
        primo = 1
        for candidato_a_divisor in primos_no_intervalo.values():
            if candidato_a_divisor > int(numero_analisado ** (1 / 2)):
                break
            if numero_analisado % candidato_a_divisor == 0:
                primo = 0
                break
        if primo:
            quant_primos += 1
            primos_no_intervalo[quant_primos] = numero_analisado

    global final_da_execucao_calculo
    final_da_execucao_calculo = agora()

    global inicio_da_execucao_prints_dos_numeros
    inicio_da_execucao_prints_dos_numeros = agora()

    for k, numero in primos_no_intervalo.items():
        print(f'{numero:>10}', end=' ')
        if k % 12 == 0:
            print()
    print()
    print(f'\n\n\nSão {len(primos_no_intervalo)} números primos no intervado entre 1 e {limite_intervalo}:')

    global final_da_execucao_prints_dos_numeros
    final_da_execucao_prints_dos_numeros = agora()


calc_quant_primos(final_intervalo)
print(f'tempo que levou para executar tudo: {agora() - inicio_da_execucao_tudo}')
print(f'tempo que levou para executar calculos: {final_da_execucao_calculo - inicio_da_execucao_calculo}')
print(f'tempo que levou para executar prints: {final_da_execucao_prints_dos_numeros - inicio_da_execucao_prints_dos_numeros}')



