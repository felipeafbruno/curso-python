# Conversão implicita 
# Conversão Automática
print(10 / 2)

# Mesmo um calculo que retorna um valor inteiro acaba sendo convertido para um float/real pelo python
print(type(10 / 2))

# Essa operação vai gerar sim um valor inteiro
print(type(10//3))  

# Essa operação vai gerar sim um valor float/real
print(type(10//3.3))

# Python resolve automaticamente True para o valor 1
print(2 + True)
# Python resolve automaticamente False para o valor 0
print(2 + False)

# Essa operação vai gerar sim um valor float/real
print(type(1 + 2.5))
