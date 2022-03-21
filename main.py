from csv import extract_data
from db import input_data

name = 'claim_sort'
column = ['1', '2', '3', '3', '3', '3']

## 엑셀 추출 데이터를 리스트로 만들고 change_to_sql >> input_data로 넘겨주면 끝


def change_to_sql(table_name, column_data):
    sql =  'INSERT INTO ' + table_name + 'VALUES ('
    for i in column_data:
        sql += "'" + i + "',"
    sql = sql[:-1] + ')'
    return sql

test = change_to_sql(name, column)
# input_data(test) 
# input_data(s)
# if(str(type(b)) == "<class 'int'>"):



