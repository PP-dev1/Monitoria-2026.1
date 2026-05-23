def saudar(nome):
    print(f'Prazer, {nome}')


# saudar(input('Qual seu nome?\n'))

def somar(n1, n2):
    resultado = n1 + n2
    return resultado


def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def somar_lista(*numeros):
    resultado = 0
    for n in numeros:
        resultado += n
    return resultado


somas = somar_lista(6, 2, 7, 9)


# print(f'O resultado é: {somas}')

def calcular_media(*numeros):
    qtd = len(numeros)
    soma = 0
    for num in numeros:
        soma += num
    media = soma / qtd
    return media


# print(calcular_media(7, 2, 4, 9))

def informacoes_pessoais(**informacoes):
    for chave, valor in informacoes.items():
        print(f'{chave}: {valor}')

informacoes_pessoais(nome = 'Pedro Paulo', idade = 19)

