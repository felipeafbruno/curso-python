# First Class Function(Função de Primeria Classe) 
'''
    Python trata funções como dados
    permitindo que a função seja armazenada
    em uma variável
'''
def dobro(x):
    return x ** 2


def quadrado(x):
    return x ** 2


if __name__ == '__main__':
    # Retorna alternadamente o dobro e o quadrado dos números de 1 a 10
    # nesse situação a lista é multiplica 5 vezes
    # [dobro, quadrado], [dobro, quadrado], [dobro, quadrado]...
    funcs = [dobro, quadrado] * 5

    # zip() retorna uma tupla de iterator baseado no objeto iterável
    # zip(funcs, range(1, 11)) ->
    # retorna uma tupla com (função, valor) - Exemplo: (dobro, 1), (quadrado, 2)...
    for func, numero in zip(funcs, range(1, 11)):
        print(f'O {func.__name__} do número {numero} é {func(numero)}')
