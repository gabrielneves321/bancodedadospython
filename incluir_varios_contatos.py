from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Bia', '98907-4323'),
    ('Ana', '98085-4456'),
    ('Tom', '98875-4390'),
    ('Mel', '97765-4356'),
    ('beca', '98225-4456'),
    ('Jão', '93365-4765'),
    ('Leco', '95565-4098'),
)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')