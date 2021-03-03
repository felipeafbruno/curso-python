from db import nova_conexao


sql = 'SELECT nome, tel FROM contatos'


with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for contato in cursor:
        print(f'\t'.join(str(campos) for campos in contato))