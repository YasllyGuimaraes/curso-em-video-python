#(008)Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Uma distancia em metros: '))
print('A medida de {}m corresponde a:')
print(f'{(m/1000)}km\n{(m/100)}hm\n{(m/10)}dam\n{(m*10)}dm\n{(m*100)}cm\n{(m*1000)}mm')

