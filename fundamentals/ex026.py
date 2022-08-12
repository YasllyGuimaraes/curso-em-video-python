'''(026) Fça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez
'''

frase = str(input('Digite uma frase: ')).strip().upper()

f = frase.count('A')
f1 = frase.find('A')
f2 = frase.rfind('A')

print(f'A letra A aparece {f} vezes na frase.')
print(f'A primeira letra A aparece na posição {f1 + 1}.')
print(f'A última letra A aparece na posição {f2 + 1}.')


