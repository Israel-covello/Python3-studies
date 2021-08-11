# ex-094 - Unindo Dicionários e listas

lista = list()
dados = dict()
total = 0

while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if dados['sexo'] not in 'FM':
            print('ERRO! Responda apenas F ou M.')
        else:
            break
    dados['idade'] = int(input('Idade: '))
    total += dados['idade']
    lista.append(dados.copy())
    resposta = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while True:
        if resposta not in 'SN':
            resposta = str(input('ERRO! Responda apenas com S ou N!\nDeseja continuar [S/N]? ')).strip().upper()[0]
        else:
            break
    if resposta == 'N':
        break
media = total / len(lista)
print(f'{"Dados Cadastrados":^20}')
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print(end='')
        for k, v in p.items():
            print(f'{k} = {v}')
        print()
