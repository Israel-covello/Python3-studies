# ex-090 - Dicionário

aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'Digite a média do aluno {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for key, value in aluno.items():
    print(f'{key} = {value}')
