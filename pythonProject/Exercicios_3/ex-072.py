# ex-072 - Números por Extenso

lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
            'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
        'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
            'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('Tente novamente!')
    print(f'O número {num} escrito por extenso é {lista[num]}!')
    while True:
        sair = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if sair not in 'SN':
            print('INVALIDO! ', end='')
        else:
            break
    if sair == 'N':
        break
print('Programa Finalizado!!!')
