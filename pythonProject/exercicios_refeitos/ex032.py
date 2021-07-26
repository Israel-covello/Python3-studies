ano = int(input('Digite um ano para saber se ele é BISEXTO: '))
if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print('O ano de {} é BISEXTO!'.format(ano))
else:
    print('O ano NÃO é BISEXTO!')
