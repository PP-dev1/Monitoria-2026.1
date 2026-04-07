# numeros pares entre 100 e 168


num = 100
while num <= 168:
    if num %2 == 0:
        print(f'O número {num} é par')
    else:
        print(f'O número {num} é ímpar')
    num += 1