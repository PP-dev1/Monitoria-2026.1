num = int(input('Insira um número: '))

centenas = num // 100
resto = num - centenas * 100
dezenas = resto // 10
unidades = resto - dezenas * 10
print(f'{num} = {centenas} Centenas {dezenas} Dezenas {unidades} Unidades')

