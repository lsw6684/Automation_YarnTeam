import pymssql
import db_info
def input_data(table_name, column_data):

    # SQL로 전환
    sql =  'INSERT INTO ' + table_name + 'VALUES ('
    for i in column_data:
        sql += "'" + i + "',"
    sql = sql[:-1] + ')'

    # DB 서버 주소
    server = db_info.server_address

    # DB 이름
    database = db_info.db_name

    # 접속 ID, PW
    username = db_info.username
    password = db_info.password

    # MSSQL 접속
    connected_db =  pymssql.connect(server , username, password, database, charset='EUC-KR') # 
    connected_db.autocommit(True) # 자동 커밋
    cursor = connected_db.cursor()

    # 명령
    cursor.execute(sql)
    
    # 연결 종료
    connected_db.close()