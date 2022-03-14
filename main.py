import pandas as pd

xlsx = pd.read_excel('./../files/title.csv') # nrows : 가져올 row 수, skiprows : sip할 row 수

Sub1_list = xlsx.iloc[2:, 1].values.tolist()
print(xlsx)
print(Sub1_list)