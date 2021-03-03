try:
    from mysql import connector
except ModuleNotFoundError:
    print('MYSQL connector não esta instalado.')
else:
    print('MYSQL connector instalado e pronto.')

    