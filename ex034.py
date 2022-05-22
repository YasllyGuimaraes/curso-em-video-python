'''(034) Escreva um programa que pergunte o salário de um funcionário e calcule ovalor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para inferiores ou iguais , o aumento é de 15%.
'''

salario = float(input('Qual o salário do funcionário? '))

if salario > 1250:
    novo_salario = salario + salario * (10/100)
else:
    novo_salario = salario + salario * (15/100)

print(f'Quem ganhava {salario:.2f} passa a ganhar {novo_salario:.2f} agora.')

