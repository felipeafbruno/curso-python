# Quarta versão do projeto
# Fibonacci com limite definido na condição do laço while 
def fibonacci(limite):
    resultado = [0, 1] # Lista
    while resultado[-1] < limite: # verificando se o valor da ultima posição da lista é maior que o limite imposto
        resultado.append(resultado[-2] + resultado[-1]) # penultima posição + ultima posição
    return resultado


if __name__ == '__main__':
    for valor_fibonacci in fibonacci(100):
        print(valor_fibonacci)