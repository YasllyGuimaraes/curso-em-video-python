'''(056) Desenvolva um programa que leia um nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é nome do homem mais velho
- Quantas mulheres têm menos de 20 anos.  '''

soma_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
tot_mulher_20 = 0

for i in range(1, 5):
    print(f'---------- {i}° PESSOA ----------')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).upper()

    soma_idade = soma_idade + idade

    if i == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_mais_velho = nome

    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome

    if sexo =='F' and idade < 20:
        tot_mulher_20 = tot_mulher_20 + 1

print(f'A média de idade do grupo é {soma_idade / 4}')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho}.')
print(f'Ao todo são {tot_mulher_20} mulheres com menos de 20 anos.')
