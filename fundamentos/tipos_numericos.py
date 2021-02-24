# print(dir(int))
# print(dir(float))

a = 5
b = 2.5
# Retorno do tipo Float
print(a / b)
print(a + b)
print(a * b)

print(b.is_integer())
print(5.0.is_integer())
print(int.__add__(2, 3))
print((-2).__abs__()) # função interna do int
print((-3.6).__abs__()) # função interna do float