from functools import reduce


# Recursividade
# Criado um método calc() recebendo um parametro divisor
# return passa o resultado divisor se a soma do map de resto de divisão de
# x por divisor com base na list 'numeros' dor igual a 0
# caso contrario calc é chamada novamente passando divisor -1 e assim por diante   
def mdc(numeros):
    def calc(divisor):
       return divisor if sum(map(lambda x: x % divisor, numeros)) == 0 \
            else calc(divisor = -1)
    return calc(min(numeros))


if __name__ == '__main__':
    print(mdc([21, 7])),
    print(mdc([125, 40])),
    print(mdc([9, 254, 66, 3])),
    print(mdc([55, 22])),
    print(mdc([15, 150])),
    print(mdc([7, 9]))
