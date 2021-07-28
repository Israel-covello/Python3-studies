# ex-074 - Maior e Menor valores em Tupla

from random import randint
sort = (randint(0, 10), randint(0, 10), randint(0, 10),
        randint(0, 10), randint(0, 10))
print(f'Números sorteados: {sort}')
print(f'O maior é {max(sort)} e o menor é {min(sort)}')
