frase = str(input('Digite um frase: ')).upper().strip()
print('Na frase aparece {} letras A. Primeira vez na {} posição, segunda ves na {} posição!'
      .format(frase.count('A'), frase.find('A') + 1, frase.rfind('A') + 1))
