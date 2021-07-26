salario = float(input('Digite o seu sálario: '))
if salario > 1250:
    print('Seu salario tem um aumento de 10%. Ficara R${:.2f}'.format(salario + (salario * 10 / 100)))
else:
    print('Seu salario tem um aumento de 15%. Ficara R${:.2f}'.format(salario + (salario * 15 / 100)))
