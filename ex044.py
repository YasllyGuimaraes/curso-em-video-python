'''(044) Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto.   - Em até 2x no cartão: preço normal.
- À vista cartão: 5% de desconto.             - 3x ou mais no cartão: 20% de juros. '''

print('========== LOJAS GUANABARA ==========')
preco = float(input('Preço das compras: R$'))
print('FORMA DE PAGAMENTO')
print('''[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    preco_desconto = preco - (preco * (10 / 100))
    print(f'Sua compra de R${preco} vai custar R${preco_desconto} no final.')

elif opcao == 2:
    preco_desconto = preco - (preco * (5 / 100))
    print(f'Sua compra de R${preco} vai custar R${preco_desconto} no final.')


elif opcao == 3:
    valor_parcela = preco / 2
    print(f'Sua compra será parcelada em 2x de {valor_parcela:.2f} SEM JUROS.')
    print(f'O valor da sua compra é R${preco}.')

elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor_total = preco + (preco * (20 / 100))
    valor_parcela = valor_total / parcelas
    print(f'Sua compra será parcela em {parcelas}x de R${valor_parcela:.2f} COM JUROS.')
    print(f'Sua compra de R${preco} vai custar R${valor_total} no final.')

else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')


