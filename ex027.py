'''(027) Faça um programa que leia o nome completo de uma pessoa. Mostrando em seguida o primeiro e o último nome
separadamente
Exemplo: Ana Maria de Souza
- primeiro: Ana
- último: Souza
'''

nome = str(input('Digite seu nome completo: ')).strip()
n1 = nome.split()[0]
n2 = nome.split()[-1]
print(f'Seu primeiro nome é {n1}')
print(f'Seu último nome é {n2}')
