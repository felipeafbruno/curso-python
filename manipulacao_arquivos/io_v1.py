# open() -> utilizado para abrir o arquivo passado como parametro
arquivo = open('./manipulacao_arquivos/pessoas.csv')
dados = arquivo.read()  # read() -> leitura do arquivo
arquivo.close()  # close() -> fechando o arquivo


# cada uma das linha separadas - splitlines() quebra os registros em linhas
for registro in dados.splitlines():
    # '*' -> indica argumentos variáveis
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
