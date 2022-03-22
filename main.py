from datetime import datetime
from csv_extraction import extract_data
from db import input_data

name = 'claim_sort'
column = ['1', '2', '3', '3', '3', '3']
excel_title = 'CHINA_COTTON'

# 엑셀 추출 데이터를 리스트로 만들고 
# input_data로 (테이블명, 데이터 리스트) 삽입. 
# DB insert 완료.


print(datetime.today().day)
print(datetime.today().strftime('%b'))


# print(datetime.now())


