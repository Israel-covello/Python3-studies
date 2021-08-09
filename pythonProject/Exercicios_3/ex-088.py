# ex-088 - Palpites para mega-sena

from random import randint
from time import sleep


jogos = []
tot_jogos = []
jogador = int(input('Quantos jogos você quer gerar? '))
for j in range(0, jogador):
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont == 6:
            break
    jogos.sort()
    tot_jogos.append(jogos[:])
    jogos.clear()
print(f'Sorteando {jogador} Jogos!')
for ind, lis in enumerate(tot_jogos):
    print(f'Jogo {ind+1}: {lis}')
    sleep(0.5)
print('Boa Sorte!')