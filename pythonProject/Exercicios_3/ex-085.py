# ex-085 - Lista com pares e impares

num = [[], []]
for cont in range(7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Lista completa {num}')
print(f'Lista par {num[0]}')
print(f'Lista impar {num[1]}')
