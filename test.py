import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def data():
    df = pd.read_csv("smhi-opendata-1.csv", on_bad_lines='skip', sep=';', usecols=['Lufttemperatur', 'Representativt dygn'])
    return df.values

def predicted(year):
    previous = data()
    years = []
    temps = []
    for i in previous:
        if i[0].endswith("01-01"):
            date_str = i[0]
            temp = float(i[1])
            year_val = int(date_str[:4])
            years.append(year_val)
            temps.append(temp)
    if years:
        X = np.array(years).reshape(-1, 1)
        y = np.array(temps)
        model = LinearRegression()
        model.fit(X, y)
        prediction = model.predict([[year]])[0]
        return prediction
    else:
        return None
            
            

print(predicted(2025))
