#(010)Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere 1 dólar = R$ 3,27
d = float(input('Quanto de dinheiro você tem na carteira? R$ '))
print(f'Com R$ {d} você pode comprar US {d/3.27:.2f}')
