# Terceira versão do projeto
# Fibonacci com limite definido na condição do laço while
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=",")
    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo # utilizando a troca entre variáveis
        print(ultimo, end=",")


if __name__ == '__main__':
    fibonacci(21)