
alavanca = True

if alavanca:
    print("ligar Lâmpada")

bit1 = True
bit2 = True

if bit1 or bit2:
    print('Lanterna Ligada')
else:
    print('Lanterna Desligada')

if not (bit1 or bit2):
    print("Lanterna Ligada")
else:
    print('Lanterna Desligada')

if bit1 and bit2:
    print('Lanterna Ligada')
else:
    print('Lanterna Desligada')

if not (bit1 and bit2):
    print('Lanterna Ligada')
else:
    print('Lanterna Desligada')
