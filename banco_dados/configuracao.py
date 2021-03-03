from mysql.connector import connect


conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root@root?',
    auth_plugin='mysql_native_password' # aparentemente deve ser colocado sempre o plugin auth_plugin
)

print(conexao)