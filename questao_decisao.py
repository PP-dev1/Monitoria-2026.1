# Faça um programa que calcule as raízes de uma equação do segundo grau,
# na forma ax2 + bx + c. O programa deverá
# pedir os valores de a, b e c e fazer as consistências,
# informando ao usuário nas seguintes situações:
# a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
# e o programa não deve fazer pedir os demais valores, sendo encerrado;
# b. Se o delta calculado for negativo, a equação não possui raizes reais.
# Informe ao usuário e encerre o programa;
# c. Se o delta calculado for igual a zero
# a equação possui apenas uma raiz real; informe-a ao usuário;
# d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


a = int(input('Digite A: '))
if a == 0:
    print('Está equação não é de segundo grau')

else:
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))
    delta = (b ** 2) - 4 * a * c
    if delta < 0:
        print('O delta é negativo e não possui raízes reais.')
    elif delta == 0:
        x1 = (-b +(delta ** 0.5)) / 2 * a
        print('Delta possui apenas uma raiz real: ', x1 )
    elif delta > 0:
        x1 = (-b + (delta ** 0.5)) / 2 * a
        x2 = (-b -(delta ** 0.5)) / 2 * a
        print('Delta possui duas raízes reais: ', x1, x2)
