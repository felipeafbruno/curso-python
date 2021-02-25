generator = (i ** 2 for i in range(10) if i % 2 == 0) # Generator -> gera dados sob demanda
# Generator é mais performatico que List Comprehension e utiliza menos recursos

for numero in generator:
    print(numero)