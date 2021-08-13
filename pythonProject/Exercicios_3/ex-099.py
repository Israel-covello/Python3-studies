# ex-099 - Função que retorna o maior

def maior(*num):
    cont = mai = 0
    for valor in num:
        if cont == 0:
            cont = mai
        else:
            if valor > mai:
                mai = valor
        cont += 1
    return print(mai)


