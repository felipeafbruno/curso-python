from functools import reduce


pessoas = [
    {'nome': 'Felipe', 'idade': 26},
    {'nome': 'Bernardo', 'idade': 15},
    {'nome': 'Futurna', 'idade': 15},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Gabriela', 'idade': 17},
]

so_idades = map(lambda p: p['idade'], pessoas)
menores = filter(lambda idade: idade < 18, so_idades)

# reduce -> retorna um valor que é a redução do lista ou tupla ou dicionario passado para o método
# idade: acumulador
# p: instância do objeto iterado
# 0: é o valor inicial    
soma_idades = reduce(lambda idades, idade: idades + idade, menores, 0)
print(soma_idades)
