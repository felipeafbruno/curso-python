from mysql.connector.errors import ProgrammingError
from db import nova_conexao


sql = '''
    INSERT INTO contatos 
        (nome, tel)
    VALUES
        (%s, %s)
'''
args=(
        ('Furtuna', '3333-4448'), 
        ('Felipe', '5555-6666'), 
        ('Pedro', '7777-8888'), 
        ('Bernardo', '9999-1111'), 
        ('Bernardete', '9981-1118'), 
        ('Mariana', '9971-1114'),
        ('Paulo', '9921-1418')
    )


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        # para incluir varios registros executemany()
        cursor.executemany(sql, args)
        conexao.commit()
        print('Registros inseridos com sucesso!!!')
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
