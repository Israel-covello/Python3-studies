# ex-092 - Cadastro de trabalhador

from datetime import datetime

cadastro = dict()
atual = datetime.now().year

cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['ctps'] = int(input('Carteira de trabalho: (0 não tem) '))
cadastro['idade'] = atual - nasc
if cadastro['ctps'] == 0:
    pass
else:
    cadastro['contratração'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + cadastro['contratração'] + 35 - atual
print(f'Dicionário completo:\n{cadastro}')
print(f'{"CADASTRA DO FUNCIONÁRIO":-^45}')
for k, v in cadastro.items():
    print(f'  -{k} tem valor {v}')
