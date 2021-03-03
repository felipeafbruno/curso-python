from db import nova_conexao


sql = "SELECT * FROM contatos WHERE nome LIKE '%e%'"


with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for registro in cursor:
        print(registro)
