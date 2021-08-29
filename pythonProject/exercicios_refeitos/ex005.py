num = int(input('Digite um número: '))
print('O seu numero \033[1;31m{}\033[m tem o sucessor \033[1;32m{}\033[m '
      'e o antecessor \033[1;33m{}\033[m!'.format(num, num + 1, num - 1))
