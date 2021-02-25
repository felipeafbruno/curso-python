def executar(funcao): # paramentro funcao -> callable
    if callable(funcao): # callable verifica se é uma função "chamável"
        funcao()


def bom_dia():
    print('Bom dia')


def boa_tarde():
    print('Bom tarde')


if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    executar(1)
