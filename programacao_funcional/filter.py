pessoas = [
    {'nome': 'Felipe', 'idade': 26},
    {'nome': 'Bernardo', 'idade': 15},
    {'nome': 'Futurna', 'idade': 15},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Gabriela', 'idade': 17},
]

menores = filter(lambda p: p["idade"] < 18, pessoas)
print(list(menores))

nomes_grandes = filter(lambda p: len(p["nome"]) >= 7, pessoas)
print(list(nomes_grandes))
