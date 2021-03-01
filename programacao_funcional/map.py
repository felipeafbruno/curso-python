lista_1 = [1, 2, 3]

dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'Felipe', 'idade': 26},
    {'nome': 'Bernardo', 'idade': 15},
    {'nome': 'Furtuna', 'idade': 15}
]

so_nomes = map(lambda pessoa: pessoa['nome'], lista_2)
print(list(so_nomes))

so_idade = map(lambda pessoa: pessoa['idade'], lista_2)
print(sum(so_idade))

# Desafio
def criar_descricao(pessoa):
    return f'{pessoa["nome"]} tem {pessoa["idade"]} anos'
 
descricao = tuple(map(criar_descricao, lista_2))
print(descricao)
