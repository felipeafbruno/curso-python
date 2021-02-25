# With implicitamente fecha o recurso assim que o código dentro da instrução with termina
with open('pessoas.csv') as file:
    for registro in file:
        print('Nome: {} e Idade: {}'.format(*registro.strip().split(',')))

if file.closed:
    print('Arquivo foi fechado!')
