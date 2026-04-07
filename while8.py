# Escreva um programa que leia um vetor de n coordenadas e informe se o
# vetor se encontra no primeiro ortante (ortante positivo). Nota: um vetor
# se encontra no ortante positivo se todas as suas coordenadas são números
# positivos. ORTANTE = Região no plano cartesiano

n = int(input("Quantas coordenadas o vetor tem? "))
i = 0
positivo = True # Só vai ser positivo se todos os números forem positivos

while n > i:
    valor = float(input(f'Digite a coordenada{i+1}: '))

    if valor <= 0:
        positivo = False # A variável positivo so vai ser false dps que o while acabar

    i +=1

if  positivo: # Se positivo é True, ou seja if positivo == True:
    print("O vetor está no primeiro ortante (positivo).")
else:
    print('O vetor não está no primeiro ortante (negativo)')
