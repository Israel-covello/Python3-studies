# ex-084 - Lista composta e análise de dados

lista_pessoas = list()
dados = list()
pessoas = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas += 1
    if len(lista_pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista_pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'sSnN':
        continuar = str(input('OPÇÃO INVALIDA! Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'nN':
        break
print(f'{pessoas} pessoas foram cadastradas.')
print(f'O mais pesado tem {maior}kg que é ', end='')
for p in lista_pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO mais leve tem {menor}kg que é ', end='')
for p in lista_pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
