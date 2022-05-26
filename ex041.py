'''(041) A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
 mostre sua categoria, de acordo com a idade.
- Até 9 anos: MIRIN        - Até 25 anos: SÊNIOR
- Até 14 anos: INFANTIL    - Acima: MASTER
- Até 19 anos: JÚNIOR
'''

from datetime import date
ano_nascimento = (int(input('Ano de nascimento: ')))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: MIRIN')

elif idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: INFANTIL')

elif idade <= 19:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: JÚNIOR')

elif idade <= 25:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: SÊNIOR')

elif idade > 25:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: MASTER')

