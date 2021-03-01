compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 15}
)


def calc_preco_compra(compra):
    return compra['quantidade'] * compra['preco']


# Lambda
# passando a função calc_pre_compra para o map()
totais = tuple(map(calc_preco_compra, compras))

print('Preços totais: ', totais)
print('Total geral: ', sum(totais))
