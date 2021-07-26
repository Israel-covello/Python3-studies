velocidade = float(input('Qual a velocidade do carro? '))
if velocidade >= 81:
    print('Você estava {}km/h acima da velocidade, sua multa é de R${:.2f}'.format(velocidade - 80, velocidade * 7 - 560))
print('Dirija com cuidado!')
