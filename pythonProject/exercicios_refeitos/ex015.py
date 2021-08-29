km = float(input('O carro percorreu quantos km? '))
dia = float(input('Quantos dias ele ficou alugado? '))
print('Sabendo que o carro gasta \033[1;30mR$0,15\033[m por km e \033[1;30mR$60,00\033[m '
      'por dia o total é de \033[1;30mR${}\033[m na viagem!'
      .format((km * 0.15) + (dia * 60)))
