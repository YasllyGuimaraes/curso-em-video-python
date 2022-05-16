'''(023) Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Exemplo:
    Digite um número: 1834
    unidade: 4 dezena: 3 centena: 8 milhar: 1 '''

numero = int(input('Digite um número: '))
n = str(numero)
print(f'unidade:{n[3]}  dezena:{n[2]}  centena:{n[1]}  milhar:{n[0]}')


