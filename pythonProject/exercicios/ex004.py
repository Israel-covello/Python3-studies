nome = input('Digite algo: ')
print('O tipo primitivo é?', type(nome))
print('É só espaços? ', nome.isspace())
print('É numero? ', nome.isnumeric())
print('É alfabético? ', nome.isalpha())
print('É alfanumerico? ', nome.isalnum())
print('É só letra maiuscula? ', nome.isupper())
print('É só letra minuscula? ', nome.islower())
print('Está capitalizada? ', nome.istitle())
