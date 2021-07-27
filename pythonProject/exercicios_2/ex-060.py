# ex-060 - Cálculo do Fatorial

n = int(input('Digite um número: '))
x = n
f = 1
while x > 0:
    print(f'{x}', end='')
    print(' x ' if x > 1 else ' = ', end='')
    f *= x
    x -= 1
print(f'{f}')
