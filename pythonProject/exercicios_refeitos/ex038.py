'''Exercício Python 038:
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

# RESOLUÇÃO COM WHILE

sair = False
while sair != 5:
    n1 = int(input('Digite o Primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    sair += 1
    if n1 > n2:
        print(f'O {n1} é maior que o {n2}!')
    elif n1 < n2:
        print(f'O {n1} é menor que o {n2}!')
    elif n1 == n2:
        print(f'O {n1} é ingual ao {n2}!')
print('Limite de 5 verificações!')
print('FIM DO PROGRAMA!')
