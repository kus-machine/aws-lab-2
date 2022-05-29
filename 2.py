import pandas as pd
from calendar import monthrange


data_USD = pd.DataFrame()
data_EUR = pd.DataFrame()
for month in range(1,13):
    n_day = monthrange(2022, month)[1]
    month = str(month)
    if len(month) == 1:
        month = "0" + month
    for day in range(1, n_day):
        day = str(day)
        if len(day) == 1:
            day = "0" + day
        link = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=2022" + month + day + "&json"
        try:
            df = pd.read_json(link).drop(columns=["txt", 'r030'])
            data_EUR = pd.concat([data_EUR, df[df.cc == 'EUR']]).reset_index(drop=True)
            data_USD = pd.concat([data_USD, df[df.cc == 'USD']]).reset_index(drop=True)
            print(data_EUR)
        except:
            break

# data_EUR.to_csv('data_EUR.csv')
# data_USD.to_csv('data_USD.csv')

data_EUR.to_json('/test/data_EUR.json')
data_USD.to_json('/test/data_USD.json')
