'''(065) Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os 
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

quantidade = soma = maior = menor = 0
resposta = 'S'

while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    quantidade += 1
    soma += numero
    media = soma / quantidade

    if quantidade == 1:
        maior = menor = numero

    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

print(f'Você digitou {quantidade} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')
