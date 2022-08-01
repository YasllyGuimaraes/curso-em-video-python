'''(022) Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas as lestras minúsculas.
- Quantas letras ao todo (sem considerar os espaços)
- Quantas letras tem o primeiro nome. '''

nome = str(input('Digite seu nome completo: ')).strip()
espaços = nome.count(' ')
separa = nome.split()

print(f'Seu nome em maiúsculo: {nome.upper()}')
print(f'Seu nome em minúsculo: {nome.lower()}')
print(f'Seu nome tem um total de letras igual a: {len(nome) - espaços}')
print(f'Seu primeiro nome tem um total de letras igual a: {len(separa[0])}')



