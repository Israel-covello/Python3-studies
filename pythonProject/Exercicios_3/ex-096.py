# ex-096 - Função que caucula área

def area(a, b):
    s = a * b
    return s


print('=== CAUCULO DE ÁREA ===')
lar = float(input('Largura: (m) '))
comp = float(input('Comprimento: (m) '))
print(f'A área total é de {area(lar, comp)}m²')
