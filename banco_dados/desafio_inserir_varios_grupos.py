from mysql.connector.errors import ProgrammingError
from db import nova_conexao


sql = 'INSERT INTO grupos (descricao) VALUES (%s)'
args = (
    ('casa',),
    ('trabalho',)
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
        print('INSERT realizado com sucesso!!!')
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        print(f'Quantidade de linhas inseridas: {cursor.rowcount}')
