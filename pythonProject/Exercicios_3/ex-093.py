# ex-093 - Cadastro de jogador


dados = dict()
gols = list()
dados['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas o {dados["nome"]} jogou: '))
for g in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {g+1} ele fez? ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print(f'\n{dados}\n')
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print(f'\nO jogador {dados["nome"]} jogou {partidas} partidas')
for i, v in enumerate(dados['gols']):
    print(f'  =>Na partida {i+1} fez {v} gols.')
