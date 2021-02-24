from math import pi
import sys

def circulo(raio):
    return pi * (float(raio) ** 2)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("É necessário informar o raio do círculo.")
        print("Sintaxe: {} <raio>".format(sys.argv[0][2:])) # sys.argv[0] temos o nome do arquivo chamado
    else :
        raio = sys.argv[1]
        area = circulo(raio)
        print(f'Área do circulo: {area}')