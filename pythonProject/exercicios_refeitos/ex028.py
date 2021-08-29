import random
print('Tente adivinhar o numero inteiro que estou pensando de 0 a 5!')
num = int(input('Digite um numero que você pensou: '))
n = random.randint(0, 5)
if n == num:
    print('Parabéns, tambem pensei no {}'.format(num))
else:
    print('Burrão em?! Pensei no {}!'.format(n))
