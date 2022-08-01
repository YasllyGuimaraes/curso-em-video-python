'''(064) Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
 que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''


contador = soma = numero = 0

while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    contador += 1
    soma += numero

print(f'Você digitou {contador - 1} números e a soma entre eles foi {soma - 999}.')
 
