'''Exercício Python 043:
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

# RESOLUÇÃO USANDO WHILE MOSTRANDO NO FIM QUANTIDADE DE PESSOAS EM CADA CATEGORIA

pessoa = 1
abaixo = 0
ideal = 0
sobrepeso = 0
obesidade = 0
morbida = 0

while pessoa:
    print(f'----- {pessoa}º PESSOA -----')
    peso = float(input('Digite o peso da pessoa: '))
    altura = float(input(f'Digite a altura da pessoa ou 0 para sair: '))
    pessoa += 1
    if altura > 0:
        imc = peso / (altura ** 2)
        if imc < 18.5:
            abaixo += 1
            print('ABAIXO DO PESO!')
        elif 18.5 < imc < 25:
            ideal += 1
            print('PESO IDEAL!')
        elif 25 < imc < 30:
            sobrepeso += 1
            print('SOBREPESO!')
        elif 30 > imc < 40:
            obesidade += 1
            print('OBSIDADE!')
        elif imc > 40:
            morbida += 1
            print('OBESIDADE MORBIDA!')
        pessoa = False
print(f'''São: 
{abaixo} pessoas ABAIXO do peso!
{ideal} pessoas com o peso IDEAL!
{sobrepeso} pessoas com SOBREPESO!
{obesidade} pessoas com OBESIDADE!
{morbida} pessoas com OBESIDADE MORBIDA!''')
