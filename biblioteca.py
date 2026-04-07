import pyautogui
import random
import os
import datetime
import tkinter
import pytube


qtd = int(input('escolha a quantidade de vezes a se repetir: '))
qtdV = 0
for i in range(qtd):
    numEscolha = int(input('Escolha um número de 1 a 10: \n'))
    numAleatorio = random.randint(0, 10)
    if numEscolha == numAleatorio:
        print(f'O número aleatorio foi: {numAleatorio}, vc perdeu! :(')
        break
    else:
        print(f'O nuúmero aleatório foi: {numAleatorio}, vc ganhou! :)')
        qtdV += 1

print(f'você ganhou: {qtdV} vez(es)')
