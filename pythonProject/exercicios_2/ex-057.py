# ex-057 - Validação de Dados

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while True:
    if sexo not in 'FM':
        sexo = str(input(f'Dados invalidos! Informe seu sexo novamente [M/F]: ')).strip().upper()[0]
    else:
        break
if sexo == 'M':
    print(f'Sexo {sexo}asculino registrado com sucesso!')
elif sexo == 'F':
    print(f'Sexo {sexo}eminino registrado com sucesso!')
