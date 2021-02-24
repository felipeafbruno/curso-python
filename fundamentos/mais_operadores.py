print('Operador de Membro')
# Operador de Membro
lista = ['Felipe', 'Furtuna', 'Bernardo']
print('Bernardo' in lista)
print('Furtuna' not in lista)

print('')
print('Operador de Identidade')
# Operador de Identidade
x = 3
y = x
z = 3
print(x is y)
print(y is z)
print(x is not z)

lista_a = [1,2,3]
lista_b = lista_a
lista_c = [1,2,3]
print(lista_a is lista_b)
print(lista_a is lista_c)