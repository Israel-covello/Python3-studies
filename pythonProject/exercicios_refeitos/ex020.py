from random import shuffle
a1 = str(input('Primeiro: '))
a2 = str(input('Segundo '))
a3 = str(input('Terceiro '))
a4 = str(input('Quarto: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem do sorteio é: {}'.format(lista))