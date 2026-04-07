while True:
    while True:
        num_usu = int(input("Entre com um número: "))

        if num_usu > 0:
            break
        else:
            print("Entrada inválida!")

    if num_usu % 2 == 0:
        print(f"{num_usu} é número par.")
    else:
        print(f"{num_usu} é número ímpar.")

    op = int(input("Deseja executar o programa novamente? (0 - NÃO) (1 - SIM): "))

    if op == 0:
        print("Tenha um bom dia!")
        break
    elif op == 1:
        pass

