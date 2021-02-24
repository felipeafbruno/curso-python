produto = {'nome': 'Caneta Chic', 'preco': 14.99, 'importado': True, 'estoque': 793}

for chave in produto.keys(): # key() retorna as chaves
    print(chave)

for valor in produto.values(): # values() retorna os valores 
    print(valor)

for chave, valor in produto.items(): # items() retorna um dicionário de itens chave/valor
    print(chave, "=", valor)