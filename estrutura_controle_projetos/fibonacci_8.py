# Quinta versão do projeto
# Fibonacci Recursiva
# sequencia=(0,1) -> parametro padrão caso não seja passado nada para o segundo parametro
# (0,1) é assumido como padrao
def fibonacci(limite, sequencia=(0,1)): 
    if len(sequencia) == limite:
        return sequencia  
    # fibonacci recebe como segundo parametro a soma de tuplas 
    # (sum(sequencia[-2:]),) -> dentro da tupla a soma das duas ultímas posições da tupla -2 e -1 e a ',' defini a tupla   
    return fibonacci(limite, sequencia + (sum(sequencia[-2:]),)) 


if __name__ == '__main__':
    for valor in fibonacci(21):
        print(valor)
