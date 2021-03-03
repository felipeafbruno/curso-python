from mysql.connector import connect
from contextlib import contextmanager


parametros = dict(
    host='localhost',
    port='3306',
    user='root',
    passwd='root@root?',
    auth_plugin='mysql_native_password'
)

@contextmanager # generator
def nova_conexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()