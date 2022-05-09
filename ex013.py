'''(013)Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''
ant = float(input('Qual o salário do funcionário? R$ '))
novo = ant + ((15 / 100) * ant)
print(f'Um funcionário que ganhava R${ant}, com 15% de aumento passa a recenber R${novo}.')