# ex-073 - Tuplas com times de Futebol

tabela = ('PALMEIRAS', 'Atlético-MG', 'Fortaleza', 'Bragantino',
          'Athletico-PR', 'Flamengo', 'CEARÁ', 'ATLÉTICO-GO',
          'BAHIA', 'Corinthians', 'Fluminense', 'SANTOS',
          'Juventude', 'Internacional', 'Cuiabá', 'Sport',
          'São Paulo', 'América-MG', 'Grêmio', 'Chapecoense')
print(f'A tabela completa é: {tabela}')
print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print(f'Os 4 ultimos colocados são: {tabela[-4:]}')
print(f'Os times em ordem são: {sorted(tabela)}')
print(f'A posição do Chapecoense é: {tabela.index("Chapecoense")+1}ª posição.')
