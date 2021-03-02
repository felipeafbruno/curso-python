from functools import reduce
from operator import add

# Uma maneira de forçar a imutablidade é o uso de tuplas
# Tupla é uma estruta de dado Imutável
valores = (30, 10, 25, 70, 100, 94)

# Aplicando funções que não alterão
# em nada o objeto 

# sorted() aplica a ordenação e retorna um nova lista
print(sorted(valores))
print(valores)

# valores.sort() altera a ordem dos elementos diretamente na lista
# valores.sort()
# print(valores)

print(min(valores)) # retorna o menor valor da lista
print(max(valores)) # retorna o maior valor data lista
print(sum(valores)) # soma os valores da lista
print(reduce(add, valores)) # soma os valores da lista
print(tuple(reversed(valores))) # retorna uma nova lista com os elementos invertidos
print(valores)
