# ex-078 - Maior e Menorvalor da lista.

list = []
maior = 0
menor = 0
for l in range(5):
    list.append(int(input(f'Digite um valor da pocição {l}: ')))
    if l == 0:
        maior = menor = list[l]
    else:
        if list[l] > maior:
            maior = list[l]
        if list[l] < menor:
            menor = list[l]
print(f'O Maior valor da lista é {maior} nas posições ', end='')
for i, v in enumerate(list):
    if v == maior:
        print(F'{i}... ', end='')
print()
print(f'O menor valor da lista é {menor} nas posições ', end='')
for i, v in enumerate(list):
    if v == menor:
        print(f'{i}... ', end='')
print()


