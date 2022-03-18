import pandas as pd
from test_csv import extract_data
from db import input_data

sql = """
SELECT  TOP 1 * 
FROM    dbo.acccost 
WHERE   dstyleno = '#7726'
AND     step_1 = 1 
AND     step_2 = 1 
AND     step_3 = 1
;
"""
print(input_data(sql))

print(extract_data())
