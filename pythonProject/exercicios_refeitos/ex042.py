'''Exercício Python 042:
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

# RESOLUÇÃO COM WHILE ATÉ CONSEGUIR FORMAR O TRIANGULO
f = True
while f:
    a = float(input('Digite a 1º reta: '))
    b = float(input('Digite a 2º reta: '))
    c = float(input('Digite a 3º reta: '))
    if a < b + c and b < c + a and c < a + b:
        f = False
        print('Essas retas FORMAM um triangulo!')
        if a == b == c:
            print('Esse é um triangulo EQUILATERO!')
        elif a != b != c and a != c != b:
            print('Esse é um triangulo ESCALENO!')
        else:
            print('Esse é um triangolo ISÓCELES!')
    else:
        print('Essas retas NÃO FORMAM um triangulo!')
        print('Tente novamente!')
