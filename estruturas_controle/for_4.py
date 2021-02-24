# for i in range(1,11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim')

from random import randint


def sortear_dado():
    return randint(1, 7)


def dado():
    for numero in range(1, 7):
        dado = sortear_dado()
        if numero % 2 != 0:
            continue
        elif numero % 2 == 0 and dado == numero:
            print('Acertou')
            print(f'numero do laço = {numero} e numero sorteado {dado}')
            break
    else:
        print(
            f'Não acertou o número! numero do laço = {numero} e numero sorteado {dado}')


dado()
