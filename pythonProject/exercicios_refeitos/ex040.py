'''Exercício Python 040:
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

# RESOLUÇÃO USANDO FOR COM 5 REPETIÇÕES

reprovado = 0
aprovado = 0
recuperação = 0
print('Fim do Programa!')
for n in range(1, 6):
    nota_1 = float(input(f'Digite a primeira nota do {n}º Aluno: '))
    nota_2 = float(input(f'Digite a segunda nota do {n}º Aluno: '))
    media = (nota_1 + nota_2) / 2
    if media < 5:
        reprovado += 1
    elif media > 7:
        aprovado += 1
    else:
        recuperação += 1
print(f'''{aprovado} alunos foram APROVADOS! 
{reprovado} alunos foram REPROVADOS! 
{recuperação} alunos estão de RECUPERAÇÃO!''')

