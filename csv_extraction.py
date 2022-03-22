import pandas as pd
 
def extract_data(title):
    xlsx = pd.read_csv('./../files/' + title + '.csv')

    Sub1_list = xlsx.iloc[10,:].values.tolist()
    return Sub1_list
