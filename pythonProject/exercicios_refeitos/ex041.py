'''Exercício Python 041:
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

# RESOLUÇÃO COM WHILE

from datetime import date
n = 1
mirim = 0
infantil = 0
junior = 0
senior = 0
master = 0
while n < 11:
    ano = int(input(f'Digite o ano do {n}º Atleta: '))
    data = date.today().year - ano
    n += 1
    if data <= 9:
        mirim += 1
        print('MIRIM!')
    elif data <= 14:
        infantil += 1
        print('INFANTIL!')
    elif data <= 19:
        junior += 1
        print('JUNIOR!')
    elif data <= 25:
        senior += 1
        print('SÊNIOR!')
    else:
        master += 1
        print('MASTER!')
print(f'''Dos Atletas são:
{mirim} são MIRIM!
{infantil} são INFANTIL!
{junior} são JUNIOR!
{senior} são SENIOR!
{master} são MASTER!''')
print('PROGRAMA FINALIZADO!!!')
