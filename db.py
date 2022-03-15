import pymssql

def input_data():
    # DB 서버 주소
    server = '192.168.1.9'

    # DB 이름
    database = 'business'

    # 접속 ID, PW
    username = 'sadev'
    password = 'sadev1003'

    # MSSQL 접속
    connected_db =  pymssql.connect(server , username, password, database, charset='EUC-KR') # connected_db.autocommit(True)
    cursor = connected_db.cursor()

    # 명령
    cursor.execute("""
    SELECT  TOP 1 * 
    FROM    dbo.acccost 
    WHERE   dstyleno = '#7726'
    AND     step_1 = 1 
    AND     step_2 = 1 
    AND     step_3 = 1
    ;
    """ )
    # cursor.execute('SELECT TOP 2 * FROM dbo.acccost WHERE step_1 = 1 AND step_2 = 1 AND step_3 = 1;')
    row = cursor.fetchone()

    #print(row)

    # 연결 종료
    connected_db.close()
    return row