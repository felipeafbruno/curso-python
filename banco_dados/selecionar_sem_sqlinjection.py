from db import nova_conexao


sql = "SELECT * FROM contatos WHERE nome LIKE %s"


with nova_conexao() as conexao:
    # recebendo do usuário o nome para a consulta
    nome = input('Contato localizar: ')
    # o trecho '%{nome}%' impede que algo passado para o nome seja interpretado como um SQL
    # aplicando caracteres de escape de forma que o valor passado sempre seja interpretado como string
    args = (f'%{nome}%', )
    
    cursor = conexao.cursor()
    cursor.execute(sql, args)

    for registro in cursor:
        print(registro)
