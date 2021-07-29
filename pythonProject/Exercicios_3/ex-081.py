# ex-081 - Extraindo dados de uma lista

lista = list()
cont = 0
while True:
    lista.append(int(input('Digite um número: ')))
    cont += 1
    c = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while c not in 'sSnN':
        c = str(input('Opção Invalida! Deseja continuar [S/N]? '))
    if c in 'nN':
        break
lista.sort(reverse=True)
print(f'Foram digitados {cont} números')
print(f'A ordem decrescente: {lista}')
if 5 not in lista:
    print('O 5 não foi adicionado na lista')
else:
    print('O 5 foi adicionado a lista!')
