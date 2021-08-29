# Aula de funções - parte 1

def mensagem(msg):                      #Função para mostrar uma mensagem entre duas linhas
    print('-' * 30)
    print(msg)
    print('-' * 30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de a + B = {s}')


def contador(*num):                    # Sinal de * serve para empacotar os paremetros guardando todos em num
    print(num)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
