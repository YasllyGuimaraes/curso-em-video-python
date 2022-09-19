'''(068) Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

vitoria = 0

print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PpIi':
        tipo = str(input('PAR OU ÍMPAR [P/I]? ')).upper().strip()[0]

    print(f'Você jogou {jogador} e o computador {computador}. O total deu {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1

        else:
            print('Você PERDEU!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1

        else:
            print('Você PERDEU!')
            break

    print('Vamos jogar novamente...')
print(f'GAME OVER!Você venceu {vitoria} vezes.')
