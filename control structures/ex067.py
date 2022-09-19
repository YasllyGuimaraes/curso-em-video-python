'''(067) Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
 digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

contador = 0

while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40) 

    if valor < 0:
        print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
        break

    print('-' * 30)    

    for i in range (1, 11):
        contador += 1
        print(f'{valor} x {contador} = {valor * contador}')

    print('-' * 30)    

