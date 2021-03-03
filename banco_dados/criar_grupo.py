from db import nova_conexao
from mysql.connector import ProgrammingError

criar_tabela_grupo = '''
    CREATE TABLE IF NOT EXISTS grupos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(30)
    )
'''

alterar_tabela__contato_1 = '''
    ALTER TABLE contatos ADD COLUMN grupo_id INT
'''
alterar_tabela__contato_2 = '''
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id) REFERENCES grupos(id)
'''


with nova_conexao() as conexao:
    try:
        try:
            cursor = conexao.cursor()
            cursor.execute(criar_tabela_grupo)
            cursor.execute(alterar_tabela__contato_1)
            cursor.execute(alterar_tabela__contato_2)
        except ProgrammingError as e:
            print(f'Error: {e.msg}')
    except ProgrammingError as e:
            print(f'Error na CONEXÃO: {e.msg}')