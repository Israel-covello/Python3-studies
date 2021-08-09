# Boletim com lista composta

lista = list()
while True:
    nome = str(input(' Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'\n{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=' * 25)
for ind, a in enumerate(lista):
    print(f'{ind:<4}{a[0]:<10}{a[2]:>8}')
while True:
    opc = int(input('\nMostrar notas de qualaluno? (999 para sair): '))
    if opc == 999:
        break
    if opc <= len(lista):
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
