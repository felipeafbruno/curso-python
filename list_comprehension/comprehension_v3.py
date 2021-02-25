generator = (i ** 2 for i in range(10) if i % 2 == 0) # Generator -> gera dados sob demanda
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))