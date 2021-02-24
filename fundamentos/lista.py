lista = [] # Mutavel, Dinâmico e Heterogenio
print(type(lista))
print(len(lista))
lista.append(1)
lista.append(5)
print(len(lista))

nova_lista = ['Felipe', 1, 2, 'Bernardo', 4, 'Furtuna']
print(nova_lista)
nova_lista.remove(4) # dado um elemento ele é removida da lista caso existe na mesma
print(nova_lista)
nova_lista.reverse()
print(nova_lista) # resultado é uma lista alterado com os elementos invertidos

lista_heterogenia = [1, 5, 'Furtuna', 'Bernardo', 3.1415]
print(lista_heterogenia.index('Furtuna')) # retorna o indice do valor dado
print(1 in lista_heterogenia) 
print('Furtuna' in lista_heterogenia)
print('Bernardo' not in lista_heterogenia)
print(lista_heterogenia[-1])
print(lista_heterogenia[-5])
print(lista_heterogenia[1:3])
print(lista_heterogenia[1:-1])
print(lista_heterogenia[1:])
print(lista_heterogenia[:-1])
print(lista_heterogenia[:])
print(lista_heterogenia[::2])
del lista_heterogenia[2]
print(lista_heterogenia)
del lista_heterogenia[1:]
print(lista_heterogenia)