viagem = float(input('Qual a distancia da viagem? '))
print('Sabendo que até 200km é R$0,50 e acima de 200km é R$0,45 por km...')
if viagem > 200:
    print('A viagem custou R${:.2f}'.format(viagem * 0.45))
else:
    print('A viagem custou R${:.2f}'.format(viagem * 0.50))
