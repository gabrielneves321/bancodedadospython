from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    password=''
)
print(conexao)
