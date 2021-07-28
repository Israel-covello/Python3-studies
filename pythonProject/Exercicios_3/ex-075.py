# ex-074 - Análise de dados em Tupla

num = (int(input('Digite o primeiro número: ')),
       int(input('Digite o primeiro número: ')),
       int(input('Digite o primeiro número: ')),
       int(input('Digite o primeiro número: ')))
print(f'Os valores digitados são: {num}')
print(f'O valor 9 apateceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
