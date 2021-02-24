# Tuplas são Imutáveis
# Não é possível adicionar um novo elemento, remover elementos pre-existentes, alterar um elemento pre-existentes

tupla = tuple()
# ou
tupla = ()
print(type(tupla))
tupla = ('um')
print(type(tupla)) # Uma String
tupla = ('um',)
print(type(tupla)) # Uma Tupla
print(tupla[0]) # é possível acessar um elemento da tupla apartir do indice

cores = ('verde', 'azul', 'amarelo', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:])
print(cores.index('amarelo'))
print(cores.count('azul')) # quantidade de vezes que o elemento aparece na tupla
print(len(cores))