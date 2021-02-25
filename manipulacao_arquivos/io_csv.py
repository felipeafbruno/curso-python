import csv


with open('pessoas.csv') as file:
    # reader() -> relizado todo processo de leitura e transformação do 
    # arquivo não sendo necessário executar split(), strip() ou qualquer outra coisa
    for pessoa in csv.reader(file): 
        print('Nome: {} e Idade: {}'.format(*pessoa))
