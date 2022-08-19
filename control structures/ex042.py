'''(042) Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
formado
- EQUILÁTERO: todos os lados iguais.
- ISÓCELES: dois lados iguais.
- ESCALENO: todos os lados diferentes.'''

lado_1 = float(input('Primeiro segmento: '))
lado_2 = float(input('Segundo segmento: '))
lado_3 = float(input('Segundo segmento: '))

if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_1 + lado_2:
    if lado_1 == lado_2 == lado_3:
        print('Os segmentos acima podem formar um TRIÂNGULO EQUILÁTERO.')
    elif lado_1 == lado_2 or lado_2 == lado_3 or lado_3 == lado_1:
        print('Os segmentos acima podem formar um TRIÂNGULO ISÓCELES.')
    elif lado_1 != lado_2 != lado_3:
        print('Os segmentos acima podem formar um TRIÂNGULO ESCALENO.')

else:
    print('Os seguimentos acima NÃO PODEM FORMAR UM TRIÂNGULO.')


