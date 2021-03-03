from mysql.connector.errors import ProgrammingError
from db import nova_conexao


sql_update = '''UPDATE contatos SET nome = %s where id = %s'''
# sql_update = '''UPDATE contatos SET nome = ? where id = ?''' outra possibilidade
id_consulta = input('Id do contato para atualizar:')
nome = input('Nome do contato para alteração:')
args = (nome, id_consulta)



with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        # cursor = conexao.cursor(prepared=True) define um prepared_statement 
        cursor.execute(sql_update, args)
        conexao.commit()
        print('Update realizado com sucesso!!!')
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        print(f'{cursor.rowcount} quantidade de linha(s) alterada(s).')
