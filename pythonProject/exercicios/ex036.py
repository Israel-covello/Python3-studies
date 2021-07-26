'''Exercício Python 36:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

# USANOD ESTRUTURA DE REPETIÇÃO WHILE

valor_da_casa = float(input('Digite o valor da casa: '))
salario = float(input('Sálario: '))
anos = int(input('Em quantos anos você quer paga: '))
parcela = valor_da_casa / (anos * 12)
mensal = parcela * 100 / salario
while mensal > 30:
    print(f'{mensal:.2f}% do seu sálario! Parcela de R${parcela:.2f} em {anos * 12}x')
    if mensal > 30:
        print('Negado! Tente novamente.')
        valor_da_casa = float(input('Digite novamente o valor da casa: '))
        salario = float(input('Digite novamente o sálario: '))
        anos = int(input('Digite novamente em quantos anos você quer pagar: '))
        parcela = valor_da_casa / (anos * 12)
        mensal = parcela * 100 / salario
print('Você foi APROVADO!')
print(f'{mensal:.2f}% do seu sálario! Parcela de R${parcela:.2f} em {anos * 12}x')
