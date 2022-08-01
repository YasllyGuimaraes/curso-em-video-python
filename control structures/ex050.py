'''(050) Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se
o valor digitado for ímpar, desconsidere-o.'''

cont = 0

for i in range(0, 6):
    n = int(input('Digite um número: '))

    if n % 2 == 0:
        cont = cont + n

print(f'A soma de todos os números pares digitados é {cont}.')

