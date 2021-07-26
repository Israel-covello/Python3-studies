largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
print('Sabendo que a largura da parede é {}m e a altura é {}m, sua área é de \033[31m{:.2f}m²\033[m.\n'
      'Sabendo que 1l de tinta pinta 2m, a quantidade de tinta usa é de \033[31m{:.2f}l\033[m!'
      .format(largura, altura, largura * altura, largura * altura * 2))
