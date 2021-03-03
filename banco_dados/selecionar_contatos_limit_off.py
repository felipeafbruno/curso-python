from mysql.connector.errors import ProgrammingError
from db import nova_conexao


sql = 'SELECT * FROM contatos LIMIT %s OFFSET %s'
args = (5, 8)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        contatos = cursor.fetchall()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:10s} - Telefone: {contato[1]}')