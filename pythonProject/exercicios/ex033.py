a = float(input('Primeiro numero: '))
b = float(input('Segundo numero: '))
c = float(input('Terceiro numero: '))
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print('Menor é {:.0f}'.format(menor))
maior = a
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c
print('Maior é {:.0f}'.format(maior))
