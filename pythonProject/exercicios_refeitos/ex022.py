nome = str(input('Digite seu nome completo: ')).strip()
dividir = nome.split()
print('Seu nome em letra MAIUSCULA é: \033[1;30m{}\n\033[mSeu nome em letra MINUSCULA é: \033[1;31m{}\n\033[m'
      .format(nome.upper(), nome.lower()))
print('Seu nome completo tem {} letras!'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} tem {} letras'.format(dividir[0], len(dividir[0])))
