'''(042) Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre o seu status,
de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso    - 30 até 40: Obesidade
- Entre 18.5 e 25: Peso ideal       - Acima de 40: Obesidade mórbida
- 25 até 30: Sobrepeso '''

peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é {imc:.2f}')

if imc < 18.5:
    print('Você está \033[1mABAIXO DO PESO\033[m.')

elif 18.5 < imc <= 25:
    print('Você está no\033[1m PESO IDEAL\033[m.')

elif 25 < imc <= 30:
    print('Você está com \033[1mSOBREPESO\033[m.')

elif 30 < imc <= 40:
    print('Você está com \033[1mOBESIDADE\033[m.')

else:
    print('Você está com \033[1mOBESIDADE MÓRBIDA\033[m.')

