from db import nova_conexao


sql = 'SELECT * FROM contatos'


with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    contato = cursor.fetchone()
    print(f'Nome:{contato[0]:10s} \ Telefone:{contato[1]}')
