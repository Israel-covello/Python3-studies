# ex-086 - Matriz

matriz = [[], [], []]
for mat in range(9):
    m = int(input(f'Digite um valor: '))
    if mat <= 2:
        matriz[0].append(m)
    elif mat <= 5:
        matriz[1].append(m)
    else:
        matriz[2].append(m)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
