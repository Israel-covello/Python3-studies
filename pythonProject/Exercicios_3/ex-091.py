# ex-091 - Jogo de dados

from random import randint
from time import sleep
from operator import itemgetter


jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = dict()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{"RANKING":^30}')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
