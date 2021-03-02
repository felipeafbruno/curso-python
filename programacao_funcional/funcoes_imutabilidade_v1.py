from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

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
print(list(reversed(valores))) # retorna uma nova lista com os elementos invertidos
print(valores)
