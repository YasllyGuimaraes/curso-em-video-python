'''(052) Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

numero = int(input('Digite um número: '))
total = 0

for i in range(1, numero + 1):

    if numero % i == 0:
        print(i, end=' ')
        total = total + 1
    else:
        print(i, end=' ')

print(f'\nO número {numero} é divisível {total} vezes.')

if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')




