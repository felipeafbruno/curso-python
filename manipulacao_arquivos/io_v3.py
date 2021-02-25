arquivo = open('pessoas.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(','))) # função strip() retirando espaços em branco

arquivo.close()
