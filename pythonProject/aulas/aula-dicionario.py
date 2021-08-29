# Aula 19 - Dicionários


var = dict() or {}       #---> Declarando Dicionário
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])     # = Pedro
print(dados['idade'])    # = 25
dados['Sexo'] = 'M'      # Adicionando elementos
del dados['idade']       # Deletando elemento
print(dados.values())    # Metodo interno que retorna os valores ('Pedro' 'M')
print(dados.keys())      # Metodo interno que retorna as chaves ('Nome' 'Sexo')
print((dados.items()))   # Metodo interno que torna os itens ('nome', 'Pedro'), ('Sexo', 'M')
dados.copy()             # Metodo interno para copiar, substituindo o [:] usado em listas

for k, v in dados.items():    # Metodo
    print(f'O {k} é {v}')


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    print(e)             # Retorna cada Dicionári separado
    for k, v in e.values():
        print(f'O campo {k} tem valor {v}')      # Retorna os formatados
    for v in e.values():
        print(f'{v} ', end='')                   # Retorna só os valores formatado
    print()
