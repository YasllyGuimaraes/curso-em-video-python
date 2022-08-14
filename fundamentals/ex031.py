'''(031) Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.'''

distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}km')
if distancia <= 200:
    preço = 0.50 * distancia
    print(f'E o preço da sua passagem é R${preço:.2f}')
else:
    preço = 0.45 * distancia
    print(f'E o preço da sua passagem é R${preço:.2f}')