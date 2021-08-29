cidade = str(input('Digite o nome de uma cidade: ')).upper()
dividir = cidade.split()
if dividir[0] == 'SANTO':
    print('Sim sua cidade começa com Santo')
else:
    print('Não, sua cidade começa com {}'.format(dividir[0]))
