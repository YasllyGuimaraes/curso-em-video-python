'''(060) Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120 '''

from math import factorial

num = int(input('Digite um número para calcular seu fatorial: '))

f = factorial(num)
c = num 

while c > 0:
    print(f'{c}', end=' ')
    print(f'x' if c > 1 else ' = ', end=' ')
    c = c - 1

print(f)
