# Faça um programa que leia 5 números e informe o maior número.


n1 = input('Digite um número: ')
n2 = input('Digite um número: ')
n3 = input('Digite um número: ')
n4 = input('Digite um número: ')
n5 = input('Digite um número: ')

if n1 > n2 > n3 > n4 > n5:
    print(n1)
elif n2 > n1 > n3 > n4 > n5:
    print(n2)
elif n3 > n1 > n2 > n4 > n5:
    print(n3)
elif n4 > n1 > n2 > n3 > n5:
    print(n4)
elif n5 > n1 > n2 > n3> n4:
    print(n5)
