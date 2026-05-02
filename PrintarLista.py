produtos = [['LEITE', 10, 30.0], ['OVO', 30, 10.0]]

# for p in range(len(produtos)):
#     print(f'ITEM: {produtos[p][0]} | QUANTIDADE: {produtos[p][1]} | PREÇO: {produtos[p][2]}')
#     print('------------------')

busca = input('Digite o nome do produto: ').upper()

for p in range(len(produtos)):
    if busca in produtos[p]:
        print(produtos[p])
