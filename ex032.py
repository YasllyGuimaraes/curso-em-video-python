'''(032) Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO. '''

from datetime import date

ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual :  '))
resto = ano % 4

if ano == 0:
    ano = date.today().year
if resto == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano de {ano} NÃO É BISSEXTO')

