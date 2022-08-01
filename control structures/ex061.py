'''(061) Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma P.A, mostrando o s 10 primeiros termos da progressão usando a estrutura 
while. '''

print('GERADOR DE P.A')
print('-=' * 10)

termo_1 = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A: '))

termo = termo_1
contador = 1
while contador <= 10:
    contador += 1
    print(f'{termo}', end=' ' )
    print('->' if contador <= 10 else '', end=' ' )
    termo += razao
