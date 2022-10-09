'''(072) Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

tupla = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))

    if 0 <= numero <= 20:
            print(f'Você digitou o número {tupla[numero]}.')
    
    else:
            print('Tente novamente. ', end='')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? ')).upper().strip()[0]

    if resp == 'N':
        print('Fim')
        break
