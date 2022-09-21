'''(069) Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o 
usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos. '''

mais_de_18 = 0
homens = 0
mulher_menos_de_20 = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]

    if idade > 18:
        mais_de_18 += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulher_menos_de_20 += 1
    
    if resp == 'N':
        break

print(f'O total de pessoas com mais de 18 anos é {mais_de_18}.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulher_menos_de_20} mulheres com menos de 20 anos.')
        

