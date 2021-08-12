# ex-098 - Função de contador

def contador(i, f, p):
    cont = i
    while cont <= f:
        print(f'{cont} ', end='')
        cont += p
    print('Fim.')


contador(1, 10, 1)
