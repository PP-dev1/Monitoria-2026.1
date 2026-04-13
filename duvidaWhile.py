condicao = True
contador = 0
condicao1 = True

while condicao:
    if contador == 4:
        condicao1 = False
        print(condicao1)
        break
    else:
        contador += 1

print(condicao1)