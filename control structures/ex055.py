'''(055) Faça um programa que leia o peso de cinco pessoas. No finalç, mostre qual foi o maior e o menor peso lidos.'''

maiorpeso = 0
menorpeso= 0

for i in range(1, 6):
    peso = float(input(f'Peso da {i}° pessoa: '))
    if i == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso

print(f'O maior peso lido foi de {maiorpeso}Kg.')
print(f'O menor peso lido foi de {menorpeso}Kg.')
