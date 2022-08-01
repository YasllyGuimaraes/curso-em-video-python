'''(037) Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
de conversão:
1 - Para binário
2 - Para octal
3 - Para hexadecimal '''

numero = int(input('Digite um número: '))
print('''Escolha uma das bases para a conversão: 
[ 1 ] PARA CONVERTER PARA BINÁRIO.
[ 2 ] PARA CONVERTER PARA OCTAL.
[ 3 ] PARA CONVERTER PARA HEXADECIMAL.''')
opcao = int(input('Digite a sua opção: '))

if opcao == 1:
    print(f'{numero} convertido para \033[1;33mBINÁRIO\033[m é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para  \033[1;33mOCTAL\033[m é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido para  \033[1;33mHEXADECIMAL\033[m é {hex(numero)[2:]}')
else:
    print('Opção inválida, tente novamente!')




