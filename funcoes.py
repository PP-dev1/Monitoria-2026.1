def saudar(nome):
    print(f'Prazer, {nome}')


# saudar(input('Qual seu nome?\n'))

def somar(n1, n2):
    resultado = n1 + n2
    return resultado

# print(somar('Pedro ', 'Paulo'))

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# verificar_par(2)


def somar_numeros(*numeros):
    resultado = 0
    for n in numeros:
        resultado += n
    return resultado


# print(somar_numeros(10, 20, 30, 40))


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
    print(informacoes)
    for chave, valor in informacoes.items():
        print(f'{chave}: {valor}')

informacoes_pessoais(nome = 'Pedro Paulo', idade = 19)

