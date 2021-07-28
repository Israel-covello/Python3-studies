# ex-077 - Contando vogais em Tuplas

palavras = ('Aprender', 'Programa', 'Linguagem', 'Python',
            'Curso', 'Gratis', 'Estudar', 'Praticar',
            'Trabalhar', 'Mercado', 'Programador', 'Futuro')
for p in palavras:
    print(f'\nA palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra.upper()}', end=' ')
