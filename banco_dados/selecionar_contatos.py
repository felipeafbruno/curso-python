from mysql.connector.errors import ProgrammingError
from db import nova_conexao


sql = 'SELECT * FROM contatos LIMIT'


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        # cursor.fetchall(): 
        # retorna uma tupla com todas as linhas
        # do resultado da query SELECT
        contatos = cursor.fetchall()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        for contato in contatos:
            # '2d' - limita o valor para dois digitos
            # '20s' - limite o texto para vinte digitos 
            print(f'{contato[2]:2d} - {contato[0]:10s} - Telefone: {contato[1]}')