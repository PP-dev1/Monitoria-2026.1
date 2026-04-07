qtd_kwh = float(input("Insira a quantidade de KWH consumidos no mês: "))
bandeira = input('Digite a bandeira: ').lower() # BANDEIRA = bandeira

if qtd_kwh <= 100:
    kwh = 0.50
if qtd_kwh <= 200:
    kwh = 0.70
else:
    kwh = 0.90

valor = kwh * qtd_kwh

if bandeira == 'verde':
    acresc = 0
elif bandeira == 'amarela':
    acresc = valor * 0.10
elif bandeira == 'vermelha':
    acresc = valor * 0.20

valor_total = valor + acresc
print(f'No total, sua conta de energia deu: {valor_total:.2f}')



