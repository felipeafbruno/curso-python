# Quinta versão do projeto
# Fibonacci com limite definido na condição do laço while 
def fibonacci(limite):
    resultado = [0, 1] # Lista
    while resultado[-1] < limite: # verificando se o valor da ultima posição da lista é maior que o limite imposto
        resultado.append(sum(resultado[-2:])) # função sum() passando a lista resultado no intervalo da posição -2 a -1 como parâmetro
    return resultado


if __name__ == '__main__':
    for valor_fibonacci in fibonacci(21):
        print(valor_fibonacci)