'''Exercício Python 044:
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''


# RESOLUÇÃO USANDO LOOP FOR OU WHILE LENDO 5 PRODUTOS E SOMANDO
merc = 'S'
soma_produto = 0
while merc == 'S':
    produto = float(input('Digite o valor do produto: '))
    merc = str(input('Deseja adicionar outro produto [S/N]? ')).upper().strip().upper()
    soma_produto += produto
    if merc == 'N':
        print('''Condições de pagameto:
        [ 1 ] à vista dinheiro/cheque:
        [ 2 ] à vista no cartão: 
        [ 3 ] em até 2x no cartão:
        [ 4 ] 3x ou mais no cartão''')
        pagamento = int(input('Qual sua opção? '))
        if pagamento == 1:
            total = soma_produto - (soma_produto * (10/100))
            print(f'Pagamento a vista dinheiro/cheque! Total R${total}')
        elif pagamento == 2:
            total = soma_produto - (soma_produto * (5/100))
            print(f'Pagamento à vista no cartão! Total R${total}')
        elif pagamento == 3:
            total = soma_produto / 2
            print(f'Pagamento em 2x no cartão! 2x de R${total}')
        elif pagamento == 4:
            cartao = int(input('Pagamento no cartão! Quantas vezes? '))
            produto = soma_produto + (soma_produto * (20/100))
            total = produto / cartao
            print(f'Pagamento em {cartao}x de R${total}! Total R${produto}')
        else:
            merc = 'S'
            print('Opção invalida! Tente novamente')
print('Programa FINALIZADO!')
