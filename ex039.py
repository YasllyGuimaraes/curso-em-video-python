'''(039) Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele
ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu
programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em 2022.')

if idade < 18:
    anos = 18 - idade
    print(f'Ainda faltam {anos} para o alistamento.')
    print(f'Seu alistamento será em {ano_atual + anos}.')

elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade > 18:
    anos = idade - 18
    print(f'Você já deveria ter se alistado a {anos} anos.')
    print(f'Seu alistamento foi em {ano_atual - anos}.')


