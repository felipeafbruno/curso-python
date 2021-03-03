from db import nova_conexao
from mysql.connector.errors import ProgrammingError


excluir_tabela_emails = ''' DROP TABLES IF EXISTS emails '''

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(excluir_tabela_emails)
        print('Tabela emails excluida!!!')
    except ProgrammingError as errors:
        print(f'Erro: {errors.msg}')
