dados = list()
dados.append('Israel')
dados.append(26)

galera = list()
galera.append(dados)       # Copiando a lista [:] - Jogando uma lista dentro da outra!

galera.append(dados[:])           # Jogando mais uma lista dentro da outra (Ficara com duas listas dentro de galera)
dados[0] = 'Maria'              # Mudando o nome da segunda lista(dados) adicionada
dados[1] = 15                    # Mudando a idade da segunda lista(dados) adicionada

                  # Se quiser adicionar outra lista dentro da lista galera
                   # pode clonar a segunda lista(dados) colocando o [:]
                    # ou criar outra lista declarando ela com list()

                    # usando esse metodo
'''                 add = list()
                    add.append('João')
                    add.append(65)
                    galera.append(add)
'''
# ou clonando a lista anterior com [:] e adicionando como esta logo abaixo
galera.append(dados[:])
dados[0] = 'João'
dados[1] = 65

# Adicionando mais uma lista(dados) com o metodo [:]
galera.append(dados[:])
dados[0] = 'Victoria'
dados[1] = 8

# Observar que sempre o ultimo adicionado será o primeiro no indice da lista
print(galera)
print('-=' * 35)


for pessoa in galera:     # Mostrando as listas separadas
    print(pessoa)          # colocando o indice [0] ou [1] - mostrara somente o escolhido dentro da lista
print('-=' * 15)

# Adicionando dados em uma lista usando uma outra lista auxiliar com o [:]
lista = list()
preencher = list()
for cont in range(0, 3):
    preencher.append(str(input('Nome: ')))
    preencher.append(int(input('Idade: ')))
    lista.append(preencher[:])                # Vai adicionando o clone na lista
    preencher.clear()                          # Vai limpando a lista depois de adicionada
print(lista)

# Identificando se as pessoas cadastradas são maiores de idade
for pessoa in lista:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade!')
    else:
        print(f'{pessoa[0]} é menor de idade!')