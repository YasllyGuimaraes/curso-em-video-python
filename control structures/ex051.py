'''(051) Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. No final, mostre os 10 primeiros termos
dessa progressão.'''

print('=' * 40)
print('10 termos de uma P.A')
print('=' * 40)

termo_1 = int(input('Qual o primeiro termo dessa P.A? '))
razao = int(input('Qual a razão dessa P.A? '))
termo_10 = (termo_1 + ((10 - 1) * razao))

for i in range(termo_1, termo_10 + razao, razao):
    print(i, end='...')



