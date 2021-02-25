# Quinta versão do projeto
# Fibonacci Recursiva
# sequencia=(0,1) -> parametro padrão caso não seja passado nada para o segundo parametro
# (0,1) é assumido como padrao
def fibonacci(limite, sequencia=(0, 1)):
    # operador ternario
    # é retornado sequencia caso o tamanho da sequencia seja igual ao parametro limite
    # caso contrario a função fibonacci é invocada novamente passando o limite e a soma da atual
    # tupla sequencia e a nova tupla com a soma dos dois ultimos elementos da atual tupla sequencia
    return sequencia if len(sequencia) == limite else fibonacci(limite, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    for valor in fibonacci(21):
        print(valor)
