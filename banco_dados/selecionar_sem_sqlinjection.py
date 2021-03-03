from db import nova_conexao


sql = "SELECT * FROM contatos WHERE nome LIKE %s"


with nova_conexao() as conexao:
    # recebendo do usuário o nome para a consulta
    nome = input('Contato localizar: ')
    args = (f'%{nome}%', )
    
    cursor = conexao.cursor()
    cursor.execute(sql, args)

    for registro in cursor:
        print(registro)
