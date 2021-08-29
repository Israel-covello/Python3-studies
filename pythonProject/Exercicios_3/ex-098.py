# ex-098 - Função de contador

def contador(i, f, p):
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
        print('\n')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
        print('\n')


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Inicio: '))
fim = int(input('Final: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
