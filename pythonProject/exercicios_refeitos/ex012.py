p = float(input('Digite o preço: R$'))
print('Com 5% de desconto você terá \033[1;33mR${:.2f}\033[m de \033[1;33mR${:.2f}\033[m!'
      .format(p * (5 / 100), p))
