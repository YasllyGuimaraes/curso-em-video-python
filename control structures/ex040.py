'''(040) Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida.
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

nota_1 = (float(input('Digite a primeira nota: ')))
nota_2 = (float(input('Digite a segunda nota: ')))
media = (nota_1 + nota_2) / 2
print(f'Tirando {nota_1} e {nota_2} a média do aluno foi {media:.2f}.')

if media >= 7:
    print('O aluno foi APROVADO!')

elif  5 <= media < 7:
    print('O aluno está de RECUPERAÇÃO!')

elif media < 5:
    print('O aluno está de REPROVADO!')
