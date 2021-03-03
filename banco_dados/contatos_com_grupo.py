from mysql.connector.errors import ProgrammingError
from db import nova_conexao


sql = '''
    SELECT 
        grupos.descricao AS grupo,
        contatos.nome AS contato
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, nome
'''

with nova_conexao() as conexao:
    try:
        # conexao.cursor(dictionary=True) - torna o retorno em um dicionário
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["contato"]}')
