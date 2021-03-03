from mysql.connector import connect

conexao = connect(
    host='localhost',
    port='3306',
    user='root',
    passwd='root@root?',
    auth_plugin='mysql_native_password'
)

cursor = conexao.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS agenda')