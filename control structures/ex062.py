'''(061) Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos. '''

print('GERADOR DE P.A')
print('-=' * 20)

termo_1 = int(input('Primeiro termo: '))
razão = int(input('Razão da P.A: '))

termo = termo_1
contador = 1
total = 0
mais = 10

while mais != 0 :
    total = total + mais

    while contador <= total:
        print(f'{termo} -> ', end=' ')
        termo += razão
        contador += 1
    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais? '))
    
print(f'Progressão finalizada com {total} termos mostrados.')
