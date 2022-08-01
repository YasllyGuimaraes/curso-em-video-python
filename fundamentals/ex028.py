'''(028) Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça pro usuário
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
ou perdeu. '''

from random import randint
computador = randint(0, 5) # Sorteia o número que o computador vai pensar.
print('-=-' * 20)
print('Vou pensar em número de 0 a 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? '))

if jogador == computador:
    print(f'Você venceu! O número pensado foi {computador}')
else:
    print(f'Você perdeu! Tente novamente! O número pensado foi {computador}')

