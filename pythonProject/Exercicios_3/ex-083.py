# ex-083 - Validando Expressões Matemáticas

expres = str(input('Digite uma Expressão: '))
lista = list()
for simbolo in expres:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == '(':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está invalida!')
