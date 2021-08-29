# ex-082 - Dividindo valores em várias listas.

lista = list()
lista_par = list()
lista_impar = list()
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while resp not in 'sSnN':
        resp = str(input('Opção Invalida! Deseja continuar [S/N]? '))
    if resp in 'Nn':
        break
print(f'{"Lista Completa":-^20}')
print(lista)
print(f'{"Lista Par":-^20}')
print(lista_par)
print(f'{"Lista Impar":-^20}')
print(lista_impar)
