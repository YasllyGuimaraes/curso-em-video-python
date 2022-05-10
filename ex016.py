'''(016) Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.'''
from math import trunc
n = float(input('Digite um número: '))
print(f'O número digitado foi {n} e sua porção inteira desse numero é {trunc(n)}.')