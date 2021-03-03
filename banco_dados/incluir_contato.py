from mysql.connector.errors import ProgrammingError
from db import nova_conexao


sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('Bernardo', '1111-2222')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        print('1 registro incluído, ID: ', cursor.lastrowid)