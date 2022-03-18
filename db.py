import pymssql
import secret

def input_data(sql):
    # DB 서버 주소
    server = secret.server_address

    # DB 이름
    database = secret.db_name

    # 접속 ID, PW
    username = secret.username
    password = secret.password

    # MSSQL 접속
    connected_db =  pymssql.connect(server , username, password, database, charset='EUC-KR') # connected_db.autocommit(True)
    cursor = connected_db.cursor()

    # 명령
    cursor.execute(sql)
    # cursor.execute('SELECT TOP 2 * FROM dbo.acccost WHERE step_1 = 1 AND step_2 = 1 AND step_3 = 1;')
    row = cursor.fetchone()

    #print(row)

    # 연결 종료
    connected_db.close()
    return row