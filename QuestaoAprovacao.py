nome = input("Digite seu nome: ")

n1 = float(input("Insira sua primeira nota: "))
n2 = float(input("Insira sua segunda nota: "))
n3 = float(input("Insira sua terceira nota: "))

faltas = int(input("Insira a quantidade de faltas: "))

media = (n1+n2+n3) / 3

if media >=7 and faltas <=5:
    print("Aprovado Direto!")
elif media >=5 and media <=6.9 and faltas <=5:
    print("Recuperação")

elif media >=7 and faltas >=6 and faltas <=10:
    print("Aprovado com ressalvas")
else:
    print("Reprovado")