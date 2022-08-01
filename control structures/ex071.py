'''(071) Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual
 será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
 OBS: Considere que o caixa pssui cédulas de R$50, R$20, R$10, R$1.'''

print('=' * 30)
print(f'{"BANCO CEV" :^30}')
print('=' * 30)

saque = int(input('Quanto você quer sacar?'))

total = saque
cedula = 50
total_cedula = 0
total_50 = total_20 = total_10 = total_1 = 0
    
while True:
    if total >= 50:
        total_50 += 1
        total -= 50

    elif 50 > total >= 20:
        total_20 += 1
        total -= 20

    elif 20 > total >= 10:
        total_10 += 1
        total -=10

    elif 10 > total >= 1:
        total_1 += 1
        total -= 1

    total_cedula = 0
    if total == 0:
        break

print(f'Total de {total_50} cédulas de R$50.')
print(f'Total de {total_20} cédulas de R$20.')
print(f'Total de {total_10} cédulas de R$10.')
print(f'Total de {total_1} cédulas de R$1.')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
