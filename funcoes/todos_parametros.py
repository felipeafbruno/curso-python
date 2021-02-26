# Obs:
# Definição do tutor sobre args e kwargs
# *args -> argumentos posicionais variáveis
# **kwargs -> argumentos nomeados variáveis 
def todos_parametros(*args, **kwargs): # o método pega todos os parametros de forma genérica sejam posicionais ou nomeados 
    print(f' *args -> {args}')
    print(f' *kwargs -> {kwargs}')


if __name__ == '__main__':
    todos_parametros('a', 'b', 'c')
    todos_parametros(1, 2, 3, legal=True, valor=12.99)
    todos_parametros('Bernardo', False, [1,2,3], tamanho='M', fragil=False)