# o try é um bloco onde o corpo contem um código que pode gerar algum erro
try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(registro.strip().split(','))) # função strip() retirando espaços em branco
except IndexError: # except -> se der erro ele vai ser capturado nesse ponto
    pass
finally:
    print('finally')
    arquivo.close()

if arquivo.closed:
    print('Arquivo foi fechado!')
