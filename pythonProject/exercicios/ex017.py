import math
cateto = float(input('Cateto oposto: '))
adjacente = float(input('Cateto adjacente: '))
print('Se o cateto oposto é {} e o cateto adjacente é {} a hipotenusa é: {:.2f}'
      .format(cateto, adjacente, math.hypot(cateto, adjacente)))
