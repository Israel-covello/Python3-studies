# ex-095 - Aprimorando Dicionários

time = list()
jogador = dict()
gols = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
    gols.clear()
    for g in range(partidas):
        gols.append(int(input(f'    Quantos gols na partida {g+1} ele fez? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N!')
    if resp == 'N':
        break
print('-=' * 20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual Jogador? (999 termina) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'-LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
