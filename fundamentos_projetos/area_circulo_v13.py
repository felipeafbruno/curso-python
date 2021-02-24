from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * (float(raio) ** 2)


def help():
    print("É necessário informar o raio do círculo.")
    # sys.argv[0] temos o nome do arquivo chamado
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        '''
        sys.argv[1].isnumeric() verificando se o argumento
        passado não é númerico.
        caso True chamado o help(), o print() e o sys.exit()
        com o erro de  Argumento Inválido.
        '''
        help()
        vermelho = TerminalColor.ERRO
        branco = TerminalColor.NORMAL
        print(vermelho + "O raio deve ser um valor númerico" + branco)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print(f'Área do circulo: {area}')