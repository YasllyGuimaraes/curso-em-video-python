'''(025) Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. '''

nome = str(input('Digite seu nome completo: ')).strip()
n = ('SILVA' in nome.upper())
print(f'Seu nome tem Silva? {n}')
