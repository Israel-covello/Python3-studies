'''Exercício Python 039:
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

# RESOLUÇÃO USANDO FOR COM 5 REPETIÇÕES

from datetime import date
for i in range(1, 6):
    ano = int(input(f'Digite o ano que o {i}º jovem nasceu: '))
    data = date.today().year - ano
    if data > 18:
        print(f'Ja passou {data - 18} anos de se alistar.')
    elif data < 18:
        print(f'Ainda falta {18 - data} anos para se alistar!')
    else:
        print('Agora é o momento de se alistar!')
print('Programa Finalisado!')
