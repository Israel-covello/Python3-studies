'''Exercício Python 045:
Crie um programa que faça o computador jogar Jokenpô com você.'''

# RESOLUÇÃO USANDO WHILE PARA JOGAR O QUANTO QUISER DIGITANDO "0" PARA FINALIZAR

from random import randint

print('=-' * 9)
while True:
    print('''   JO.. KEN.. PÔ..
    PEDRA   [ 1 ]:
    PAPEL   [ 2 ]:
    TESOURA [ 3 ]:
    [0] Para Sair:''')
    print('=-'*9)
    jogador = int(input('Digite uma opção: '))
    maquina = randint(1, 3)
    print('=-'*9)
    if jogador == 0:
        break
    if jogador == 1:
        if maquina == 1:
            print('EMPATE')
        elif maquina == 2:
            print('VOCÊ PERDEU')
        elif maquina == 3:
            print('VOCÊ GANHOU')
    elif jogador == 2:
        if maquina == 1:
            print('VOCÊ GANHOU')
        elif maquina == 2:
            print('EMPATE')
        elif maquina == 3:
            print('VOCÊ PERDEU')
    elif jogador == 3:
        if maquina == 1:
            print('VOCÊ PERDEU')
        elif maquina == 2:
            print('VOCÊ GANHOU')
        elif maquina == 3:
            print('EMPATE')
    else:
        print('\033[2;31mOpção Invalida!\033[m')
        break
    print('=-'*9)
print('FIM DO JOGO!')
