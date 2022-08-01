'''(054) Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.'''

from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0

for i in range(1, 8):
    ano = int(input(f'Em que ano nasceu a {i}° pessoa: '))
    idade = ano_atual - ano
    if idade >= 18:
        totmaior = totmaior + 1

    else:
        totmenor = totmenor + 1

print(f'Ao todo tivemos {totmaior} pessoas maior de idade.')
print(f'E também tivemos {totmenor} pessoas menores de idade.')
