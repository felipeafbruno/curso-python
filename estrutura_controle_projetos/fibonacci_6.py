# Quinta versão do projeto
# Fibonacci com limite while com break
def fibonacci(quantidade):
    resultado = [0, 1] # Lista
    while True: # verificando se o valor da ultima posição da lista é maior que o limite imposto
        # função sum() passando a lista resultado no intervalo da posição -2 a -1(duas ultimas posições) como parâmetro
        resultado.append(sum(resultado[-2:]))
        # verificando se a quantidade de elementos na lista resultado é igual a quantidade passado como parâmetro para função
        # caso condição verdadeira um break é executado
        if len(resultado) == quantidade: 
            break
    return resultado


if __name__ == '__main__':
    for valor_fibonacci in fibonacci(21):
        print(valor_fibonacci)