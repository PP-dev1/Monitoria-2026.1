i = 1 # 1 pq o conjunto já começa com 1
multi = False

numero = float(input(f"Entre com o número {i} do conjunto: "))

while numero >= 0:
    if numero % 10 != 0: # Verificação para saber se é multiplo de 10
        multi = True # Se for, colocar True na variavel Multi

    i += 1
    numero = float(input(f"Entre com o número {i} do conjunto: "))

if multi:
    print("Existe múltiplo de 10 neste conjunto")
else:
    print("Não existe múltiplo de 10 neste conjunto")