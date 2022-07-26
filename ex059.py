'''(059) Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
Seu programa deverá realizar a operação solicitada em cada caso.
[1] soma
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa'''

from email.headerregistry import ParameterizedMIMEHeader


primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))

opçao = 0
while opçao != 5:
    print('''    [ 1 ] soma
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')

    opçao = int(input('>>>>>> Qual é a sua opção? '))

    if opçao == 1:
        soma = primeiro_valor + segundo_valor
        print(f'A soma entre {primeiro_valor} e {segundo_valor} é {soma}')

    elif opçao == 2:
        mult = primeiro_valor * segundo_valor
        print(f'A multiplicação entre {primeiro_valor} e {segundo_valor} é {mult}')

    elif opçao == 3:
        if primeiro_valor > segundo_valor:
            maior = primeiro_valor
        else:
            maior = segundo_valor
        print(f'Entre {primeiro_valor} e {segundo_valor} o maior é {maior}')

    elif opçao == 4:
        print('Informe os números novamente:')
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))

    elif opçao == 5:
        print('Finalizando...')

    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
