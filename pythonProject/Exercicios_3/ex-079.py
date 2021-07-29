# ex-085 - Valores únicos em uma lista

lista = []
while True:
    num = (int(input('Digite um número: ')))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado a lista!')
    c = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while c not in 'sSnN':
        c = str(input('Opção Invalida! Deseja continuar [S/N]? ')).strip().upper()[0]
    if c in 'Nn':
        break
print(f'{" Lista ":-^35}')
lista.sort()
print(f'Você adicionou os números {lista}')
