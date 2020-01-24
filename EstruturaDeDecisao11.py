'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.'''

salario = float(input('Informe o salário atual R$: '))

if salario <= 280:
    novo_salario = salario + (salario * 0.2)
    print(f'''Salario sem reajuste: R$ {salario}
Percenutal de aumento: 20%
Valor do aumento: {salario * 0.2}
Novo salario: {novo_salario:.2f}
''')
elif 280 < salario < 700:
    novo_salario = salario + (salario * 0.15)
    print(f'''Salario sem reajuste: R$ {salario}
    Percenutal de aumento: 15%
    Valor do aumento: {salario * 0.15}
    Novo salario: {novo_salario:.2f}
    ''')
elif 700 <= salario < 1500:
    novo_salario = salario + (salario * 0.1)
    print(f'''Salario sem reajuste: R$ {salario}
        Percenutal de aumento: 10%
        Valor do aumento: {salario * 0.1}
        Novo salario: {novo_salario:.2f}
        ''')
elif salario >= 1500:
    novo_salario = salario + (salario * 0.05)
    print(f'''Salario sem reajuste: R$ {salario}
           Percenutal de aumento: 5%
           Valor do aumento: {salario * 0.05}
           Novo salario: {novo_salario:.2f}
           ''')
else:
    pass

