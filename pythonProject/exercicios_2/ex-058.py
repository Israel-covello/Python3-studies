# ex-058 - Jogo de Adivinha

from random import randint
computer = randint(0, 10)
print('Tente adivinhar o numero que estou pensando!')
cont = 0
while True:
    player = int(input('Digite um numero de 0 a 10: '))
    cont += 1
    if player == computer:
        break
    else:
        if player > computer:
            print('Menor..')
        elif player < computer:
            print('Maior..')
print(f'PARABÉNS! VOCÊ ACERTOU! Também pensei no {computer}')
print(f'Foram {cont} tentativas')
