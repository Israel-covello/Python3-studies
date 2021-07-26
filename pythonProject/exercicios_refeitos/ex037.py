'''Exercício Python 037:
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

    # RESOLUÇÃO COM WHILE

num = int(input('Digite um número: '))
base = 1
while base != 0:
    print('''Escolha uma opção para conveção:
    [ 0 ] Sair
    [ 1 ] Binario:
    [ 2 ] Octal:
    [ 3 ] Hexadecimal:
    [ 4 ] Outro numero:''')
    op = int(input('Opção: '))
    if op == 1:
        print(f'Seu número {num} convertido para BINARIO é {bin(num)}.')
    elif op == 2:
        print(f'Seu número {num} convertido para ICTAL é {oct(num)}.')
    elif op == 3:
        print(f'Seu número {num} convertido para HEXADECIMAL é {hex(num)}')
    elif op == 4:
        num = int(input('Digite outro número: '))
    elif op == 0:
        base = 0
    else:
        print('ERROR! Tente novamente!')
print('PROGRAMA FINALIZADO!')
