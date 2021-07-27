# ex-061 - Progressão Aritmética.

termo = int(input('Digite o Termo: '))
raz = int(input('Digite a Razão: '))
passo = termo
cont = 1
while cont <= 10:
    print(f'{passo} => ', end='')
    passo += raz
    cont += 1
print('Fim!')
