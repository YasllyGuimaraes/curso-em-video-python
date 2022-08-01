'''(011)Faça um programa que leia a largura e a altura de uma parede em metros,calcule sua área e a quantidade de tinta
necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m².'''
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print(f'Sua parede tem dimensão de {largura}x{altura} e sua área é de {area:.3f}.')
litros = area / 2
print(f'Para pintar essa parede, você precisará de {litros:.3f}l de tinta.')
