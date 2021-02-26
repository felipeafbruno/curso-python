# Possível correção para argumento padrão mutável  
def fibonacci(sequencia=None):
    # caso None a expressão é resolvida para [0,1]
    # caso contrario a expressão é resolvida para 'sequencia' por que esta preenchida
    # ou seja não esta vazio ou None
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
