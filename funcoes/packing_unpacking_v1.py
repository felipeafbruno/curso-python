def soma_2(a, b):
    return a + b

def soma_3(a, b, c):
    return a + b + c

def soma_n(*numeros): # unpacking
    soma = 0
    for n in numeros:
        soma += n
    return soma

if __name__ == '__main__':
    # packing -> pegando os parametros e impacotando e passando para a função
    print(soma_n(1))
    print(soma_n(1, 1))
    print(soma_n(1, 2, 3))
    print(soma_n(1, 2, 3, 4, 5))

    # unpacking -> desempacotando a tupla e a lista e passando como parametro 
    tupla_nums = (1,2,3,4,5,6)
    print(soma_n(*tupla_nums))

    lista_nums = (1,2,3,4,5,6,7)
    print(soma_n(*lista_nums))