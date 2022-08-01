'''(035) Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
um triângulo. '''

print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
lado_1 = float(input('Primeiro seguimento: '))
lado_2 = float(input('Segundo seguimento: '))
lado_3 = float(input('Terceiro seguimento: '))

if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_1 + lado_2:
    print('Os seguimentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')

