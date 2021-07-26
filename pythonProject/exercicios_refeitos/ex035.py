reta1 = float(input('1° Reta: '))
reta2 = float(input('2° Reta: '))
reta3 = float(input('3° Reta: '))
if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta1 + reta2:
    print('Elas formam o triangulo!')
else:
    print('Elas não formam o triangulo1')
