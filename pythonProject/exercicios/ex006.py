num = float(input('Digite um número: '))
print('Seu numero é \033[40m{}\033[m.\n'
      'O dobro é \033[40m{}\033[m.\n'
      'O triplo é \033[40m{}\033[m.\n'
      'A raiz quadrada é: \033[40m{:.2f}\033[m.'
      .format(num, num * 2, num * 3, num ** (1/2)))
