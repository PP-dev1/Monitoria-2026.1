# Escreva um algoritmo peça um número ao usuário e some somente os números que
# são maiores que 21 e menores que 70. Continue pedindo até que ele digite -1.
soma = 0

while True:
    num = int(input("Digite um número (-1  para parar): "))
    if num == -1:
        break
    elif 21 < num < 70:
        soma += num

print("Soma dos números válidos:", soma)