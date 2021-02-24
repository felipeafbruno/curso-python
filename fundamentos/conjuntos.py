  
# %%
# Conjunto não garante a ordem da inserção, não é indexado e não aceita repetição
a = {1, 2, 3}
print(type(a))
# a[0]
a = set('coddddd3r')
print(type(a))
print(a)
print('3' in a, 4 not in a)
{1, 2, 3} == {3, 2, 1, 3}

# operacoes
c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2)) # union() -> união de dois conjuntos gerando um novo conjunto 
print(c1.intersection(c2)) # intersection() -> intersecção de dois conjuntos gerando um novo conjunto
c1.update(c2) # update() -> altera o conjunto c1 adicionando o c2
print(c1)
print(c2 <= c1) # leitura -> c2 é subconjunto de c1 
print(c1 >= c2) # leitura -> c1 é superconjunto de c2

print({1, 2, 3} - {2}) # diferença entre os conjuntos
print(c1 - c2)
c1 -= {2}
print(c1)