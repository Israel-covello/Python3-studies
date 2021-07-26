real = float(input('Quanto dinheiro você tem? R$'))
print('\033[4mR${:.2f}, da pra comprar U${:.2f}!\033[m'.format(real, real / 5.03))
