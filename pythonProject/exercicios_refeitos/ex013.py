salario = float(input('O funcionário ganha: R$'))
print('Se o Funcionário recebe \033[1;34mR${:.2f}\033[m, com 15% de almento ele passa a receber \033[1;34mR${:.2f}\033[m'
      .format(salario, salario + (salario * (15 / 100))))
