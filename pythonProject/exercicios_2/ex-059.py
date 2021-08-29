# ex-059 - Criando um Menu de Opções
from time import sleep

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
while True:
    menu = int(input('''Menu:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novo Número
    [ 5 ] Sair
    => Digite a sua Opção: '''))
    if menu == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif menu == 2:
        print(f'{num1} x {num2} = {num1 * num2}')
    elif menu == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        else:
            print(f'{num2} é maior que {num1}')
    elif menu == 4:
        num1 = int(input('Digite um novo valor: '))
        num2 = int(input('Digite outro novo valor: '))
    elif menu == 5:
        break
    else:
        print('Opção invalida!')
    print('=-' * 12)
    sleep(1)
print('Programa Finalizado!')
