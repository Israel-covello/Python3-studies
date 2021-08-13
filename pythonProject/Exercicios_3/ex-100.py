# ex-100 - Função de sortear e somar
from random import randint


def sortear():
    sort = [randint(0, 9),
            randint(0, 9),
            randint(0, 9),
            randint(0, 9),
            randint(0, 9)]
    return print(sort)


def soma_par(*num):
    par = list()
    soma = 0
    for n in num:
        if n % 2 == 0:
            par.append(n)
            soma += n
    return print(f'Os pares são {par} totalizando {soma}.')
