'''(048) Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalo de 1 até 500.'''
cont = 0

for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        cont = cont + i

print(f'A soma dos números ímpares de 1 a 500 que são múltiplos de três é {cont}.')



