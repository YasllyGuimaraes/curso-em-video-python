'''(036) Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo
que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input('VALOR DO IMÓVEL: '))
salario_comprador = float(input('SALÁRIO DO COMPRADOR: '))
anos = float(input('EM QUANTOS ANOS PRETENDE PAGAR O IMÓVEL: '))
prestacao_mensal = (valor_casa / (anos * 12))
minimo = (30/100) * salario_comprador
print(f'A prestação será de R${prestacao_mensal:.2f}')

if prestacao_mensal > minimo:
    print('\033[1;31mEMPRÉSTIMO NEGADO!')
else:
    print('\033[1;32mEMPRÉSTIMO APROVADO!')



