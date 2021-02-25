# Quinta versão do projeto
# Fibonacci subistituindo while por for
def fibonacci(quantidade):
    resultado = [0, 1] # Lista
    # no range de 2 até a quantidade passado para função
    # range inicia com 2 por que já existem duas posições preenchidas na lista(posições 0 e 1)
    for _ in range(2,quantidade): 
        # função sum() passando a lista resultado no intervalo da posição -2 a -1(duas ultimas posições) como parâmetro
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for valor_fibonacci in fibonacci(21):
        print(valor_fibonacci)