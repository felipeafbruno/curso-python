from collections import defaultdict
from mysql.connector.errors import ProgrammingError
from db import nova_conexao


sql = '''
    SELECT 
        grupos.descricao AS grupo,
        contatos.nome AS nome
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, nome
'''

with nova_conexao() as conexao:
    try:
        # conexao.cursor(dictionary=True) - torna o retorno em um dicionário
        cursor = conexao.cursor(dictionary=True)
        try:
            cursor.execute(sql)
            contatos = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        # defaultdict() da um valor padrão para cada chave criada
        # e a list passada com parametro é esse valor padrão
        agrupados = defaultdict(list)
        for contato in contatos:
            agrupados[contato['grupo']].append(contato['nome'])

        print(agrupados)