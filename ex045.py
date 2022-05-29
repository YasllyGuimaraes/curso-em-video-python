'''(045) Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=-' * 15)
print(f'Computador jogou: {itens[computador]}')

if jogador == 0:
    if computador == 0:
        print(f'Jogador jogou: {itens[jogador]}')
        print('-=-' * 15)
        print('EMPATE!')
    elif computador == 1:
        print(f'Jogador jogou: {itens[jogador]}')
        print('-=-' * 15)
        print('O jogador VENCEU!')
    elif computador == 2:
        print(f'Jogador jogou: {itens[jogador]}')
        print('-=-' * 15)
        print('O computador VENCEU!')

elif jogador== 1:
    if computador == 0:
        print(f'Jogador jogou: {itens[jogador]}')
        print('-=-' * 15)
        print('O computador VENCEU!')
    elif computador == 1:
        print(f'Jogador jogou: {itens[jogador]}')
        print('-=-' * 15)
        print('EMPATE!')
    elif computador == 2:
        print(f'Jogador jogou: {itens[jogador]}')
        print('-=-' * 15)
        print('O jogador VENCEU!')

elif jogador == 2:
    if computador == 0:
        print(f'Jogador jogou: {itens[jogador]}')
        print('-=-' * 15)
        print('O jogador Venceu!')
    elif computador == 1:
        print(f'Jogador jogou: {itens[jogador]}')
        print('-=-' * 15)
        print('O computador VENCEU!')
    elif computador == 2:
        print(f'Jogador jogou: {itens[jogador]}')
        print('-=-' * 15)
        print('EMPATE!')

elif jogador != 0 or jogador != 1 or jogador !=2:
    print('JOGADA INVÁLIDA!')






