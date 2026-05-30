# 1- Crie uma função que recebe um número e faz uma contagem regressiva a partir dele





def contagem_regressiva(num):
    for n in range(num, -1, -1):
        print(n)

# contagem_regressiva(10)

# 2- Crie uma função que recebe uma lista e retorne o maior numero dela

def maior_lista(lista: list[int]):

    maior = max(lista)

    # for l in lista:
    #     if l > maior:
    #         maior = l

    return maior


lista = [-1,-2,-3,-50]

print(maior_lista(lista))



























# Gabarito:
# 1-

def cont_regres(num):
    for n in range(num, -1, -1):
        print(n)

# cont_regres(5)

# 2-
#                      (Opcional)
def maior_lista(lista: list[int]):
    # maior = max(lista) Outra forma
    maior = lista[0]
    for l in lista:
        if l > maior:
            maior = l
    return maior

# lista = [10, 20, 30, 40, 50]
# print(maior_lista(lista))