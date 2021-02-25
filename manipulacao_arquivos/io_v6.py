# With implicitamente fecha o recurso assim que o código dentro da instrução with termina
with open('pessoas.csv') as file:
    with open('pessoas.txt', 'w') as saida: # abrindo um arquivo de escrita 
        for registro in file:
            pessoa = registro.strip().split(',')
            print('Nome: {} e Idade: {}'.format(*pessoa), file=saida) # escrevendo o retorno do arquivo csv no txt aberto anteriormente 

if file.closed:
    print('Arquivo pessoas.csv foi fechado!')

if saida.closed:
    print('Arquivo saida.txt foi fechado!')
