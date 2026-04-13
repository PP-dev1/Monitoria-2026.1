num = int(input('Digite o valor a ser sacado: '))

NotasCem = num // 100
resto = num % 100
NotasCinquenta = resto // 50
resto = resto - NotasCinquenta * 50
NotasDez = resto // 10
resto = resto - NotasDez * 10
Moeda = resto // 10
print(f'{num} = {NotasCem} Nota de Cem {NotasCinquenta} Nota de Cinquenta {NotasDez}'
      f' Nota de Dez {Moeda} Moeda de um real')