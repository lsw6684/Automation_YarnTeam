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
    connected_db =  pymssql.connect(server , username, password, database, charset='EUC-KR') # 
    connected_db.autocommit(True) # 자동 커밋
    cursor = connected_db.cursor()

    # 명령
    cursor.execute(sql)
    
    # 연결 종료
    connected_db.close()