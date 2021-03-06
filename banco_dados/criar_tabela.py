from db import nova_conexao
from mysql.connector import ProgrammingError

tabela_contatos = '''
    CREATE TABLE IF NOT EXISTS contatos(
        nome VARCHAR(60),
        tel VARCHAR(40)
    )
'''

tabela_emails = '''
    CREATE TABLE IF NOT EXISTS emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
'''


with nova_conexao() as conexao:
    try:
        try:
            cursor = conexao.cursor()
            cursor.execute(tabela_contatos)
            cursor.execute(tabela_emails)
        except ProgrammingError as e:
            print(f'Error: {e.msg}')
    except ProgrammingError as e:
            print(f'Error na CONEXÃO: {e.msg}')