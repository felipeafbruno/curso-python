print(2 + 3)
print('2' + '3')
# print(2 + '3') -> Principios do Zen of Python

a = 2
b = '3'
print(type(a))
print(type(b))

# Conversão de Tipo na váriavel b (string para inteiro)
print(a + int(b))
# Conversão de Tipo na várivel a (inteiro para string)
print(str(a) + b)
# Conversão de Tipo na várivel b (string para float)
print(a + float('3.4'))
