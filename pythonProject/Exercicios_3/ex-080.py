# ex-080 - Lista ordenada sem Repetição.

lista = []
for cont in range(5):
    n = int(input('Digite um número: '))
    if cont == 0 or n > lista[-1]:            # Se cont for o primeiro 'ou' n for maior que o ultimo da lista:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'{"Lista em Ordem":-^20}')
print(f'{lista}')
