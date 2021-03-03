from mysql.connector.errors import ProgrammingError
from db import nova_conexao


sql = 'DELETE FROM contatos WHERE nome = %s'
args = ('Bernardo',)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) deletado(s).')