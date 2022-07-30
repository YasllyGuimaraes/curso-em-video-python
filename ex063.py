'''(063) Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 '''

print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)

n_termos = int(input('Quantos termos você quer mostrar? '))

termo_1 = 0
termo_2 = 1

print(f'{termo_1} -> {termo_2}', end='')

contador = 3

while contador <= n_termos:
    termo_3 = termo_1 + termo_2
    print(f' -> {termo_3}', end='')
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1
print(' -> FIM')
