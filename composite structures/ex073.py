'''(073) Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre: 
A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time de Fortaleza.'''

tupla = ('Palmeiras', 'Corinthians', 'Fluminense', 'Atlético-MG', 'Athletico-PR',
         'Flamengo', 'Internacional', 'Bragantino', 'Santos', 'São Paulo',
         'Botafogo', 'Ceará', 'Coritiba', 'Goiás', 'Amérixa-MG', 'Avaí', 
         'Cuiabá', 'Atlético-GO', 'Juventude', 'Fortaleza')

print('-=' * 30)
print(f'\nLista de times do Brasileirão: {tupla}\n')
print('-=' * 30)
print(f'Os 5 primeiros são {tupla[0:5]}')
print('-=' * 30)
print(f'Os últimos 4 colocados são {tupla[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(tupla)}')
print('-=' * 30)
print(f'O Fortaleza está em {tupla.index("Fortaleza")+ 1} posição.')
