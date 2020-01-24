'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''
        
        

valor_hora =  float(input('informe o valor da hora trabalhada: '))
total_horas =  int(input('Informe o total de horas trabalhadas: '))
print()
print()
salario_bruto = valor_hora * total_horas

if salario_bruto <= 900:
    ir = 0
    inss = salario_bruto * 0.1
    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - inss - ir - sindicato
    total_descontos = inss + sindicato + ir

    print(f'''Salário bruto: {valor_hora} x {total_horas}  : R$ {salario_bruto}
(-) IR                   : R$ {ir:.2f}
(-) INSS (10%)           : R$ {inss:.2f}
FGTS                     : R$ {fgts:.2f} 
Total de descontos       : R$ {total_descontos:.2f}
Salario Líquido          : R$ {salario_liquido:.2f}
''')

elif 900 < salario_bruto <= 1500:
    ir = salario_bruto * 0.05
    inss = salario_bruto * 0.1
    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - inss - ir - sindicato
    total_descontos = inss + sindicato + ir

    print(f'''Salário bruto: {valor_hora} x {total_horas}  : R$ {salario_bruto}
(-) IR                   : R$ {ir:.2f}
(-) INSS (10%)           : R$ {inss:.2f}
FGTS                     : R$ {fgts:.2f} 
Total de descontos       : R$ {total_descontos:.2f}
Salario Líquido          : R$ {salario_liquido:.2f}
''')

elif  1500 < salario_bruto <= 2500 :
    ir = salario_bruto * 0.1
    inss = salario_bruto * 0.1
    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - inss - ir - sindicato
    total_descontos = inss + sindicato + ir

    print(f'''Salário bruto: {valor_hora} x {total_horas}  : R$ {salario_bruto}
(-) IR                   : R$ {ir:.2f}
(-) INSS (10%)           : R$ {inss:.2f}
FGTS                     : R$ {fgts:.2f} 
Total de descontos       : R$ {total_descontos:.2f}
Salario Líquido          : R$ {salario_liquido:.2f}
''')

elif salario_bruto > 2500:
    ir = salario_bruto * 0.2
    inss = salario_bruto * 0.1
    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - inss - ir - sindicato
    total_descontos = inss + sindicato + ir

    print(f'''Salário bruto: {valor_hora} x {total_horas}  : R$ {salario_bruto}
(-) IR                   : R$ {ir:.2f}
(-) INSS (10%)           : R$ {inss:.2f}
FGTS                     : R$ {fgts:.2f} 
Total de descontos       : R$ {total_descontos:.2f}
Salario Líquido          : R$ {salario_liquido:.2f}
''')



