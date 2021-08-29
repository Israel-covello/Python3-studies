# ex-076 - Lista de preços com tuplas

print(f'{"MATERIAIS":-^39}')
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.00,
         'Mochila', 120.9,
         'Caneta', 2.3,
         'Livro', 34.9)
for l in range(len(lista)):
    if l % 2 == 0:
        print(f'{lista[l]:.<30}', end='')
    else:
        print(f'R${lista[l]:7.2f}')
