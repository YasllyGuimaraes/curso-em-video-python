'''(049) Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um
laço for.'''

n = int(input('Digite o número da tabuada que deseja visualizar: '))

for i in range(1, 11):
    total = n * i
    print(f'{n} x {i:2} = {total}')

