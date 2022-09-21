'''(070) Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
 usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato. '''

print('-' * 25)
print('LOJA SUPER BARATÃO')
print('-' * 25)

total_da_compra = mais_de_mil = mais_barato = contador = 0
nome_do_produto_barato = ''

while True:
    nome_do_produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]

    contador += 1
    total_da_compra += preço

    if preço > 1000:
        mais_de_mil += 1

    if contador == 1 or preço < mais_barato:
        mais_barato = preço
        nome_do_produto_barato = nome_do_produto

    if resp == 'N':
        break

print('-----FIM DO PROGRAMA-----')
print(f'O total da compra foi R${total_da_compra:.2f}.')
print(f'Temos {mais_de_mil} produtos custando mais de R$1.000.')
print(f'O produto mais barato foi {nome_do_produto_barato} que custa R${mais_barato:.2f}.')
