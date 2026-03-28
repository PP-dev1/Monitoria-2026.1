num = int(input('Insira um número: '))

centenas = num // 100
resto = num - centenas * 100
print(resto)
dezenas = resto // 10
print(dezenas)
unidades = resto - dezenas * 10
print(f'{num} = {centenas} Centenas {dezenas} Dezenas {unidades} Unidades')

