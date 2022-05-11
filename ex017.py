'''(017) Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo,
calcule e mostre o comprimento da hipotenusa.'''
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hip}')
