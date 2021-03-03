from db import nova_conexao


sql = 'SELECT * FROM contatos ORDER BY nome DESC'


with nova_conexao() as cconexao:
    cursor = cconexao.cursor()
    cursor.execute(sql)

    print('\r'.join(str(registro[0]) for registro in cursor))