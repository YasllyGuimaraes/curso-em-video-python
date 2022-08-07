'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse
ângulo.'''
import math
a = float(input('Digite o ângulo que você deseja: '))
ar = math.radians(a)
print(f'O ângulo de {a}° tem o SENO de {math.sin(ar):.2f}. ')
print(f'O angulo de {a}° tem o COSSENO de {math.cos(ar):.2f}')
print(f'O angulo de {a}° tem TANGENTE de {math.tan(ar):.2f}')