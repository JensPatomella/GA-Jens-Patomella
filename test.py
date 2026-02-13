import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
from datetime import datetime, timedelta

def data():
    df = pd.read_csv("smhi-opendata-1.csv", on_bad_lines='skip', sep=';', usecols=['Lufttemperatur', 'Representativt dygn'])
    return df.values

def predicted(year):
    previous = data()
    prediction = []
    mse = []
    start = datetime(2025, 1, 1)
    end = datetime(2025, 12, 31)
    current = start
    while current <= end:
        md = current.strftime('%m-%d')
        temps = []
        years = []
        c = 0
        for i in previous:
            if i[0].endswith(md):
                temp = float(i[1])
                year_val = 0 + c
                c += 1
                years.append(year_val)
                temps.append(temp)
                index = np.where(previous == i[0])
                previous = np.delete(previous, index[0] , 0)
        if len(temps) > 0:
            X = np.array(years).reshape(-1, 1)
            y = np.array(temps)
            model = LinearRegression()
            model.fit(X, y)
            prediction.append(model.predict([[year]])[0])
            mse.append()
        current += timedelta(days=1)
    return prediction
print(predicted(28))


def WriteToCSV():
    NewData = predicted(28)
    start = datetime(2025, 1, 1)
    end = datetime(2025, 12, 31)
    current = start
    dates = []
    while current <= end:
        dates.append(current.strftime('%Y-%m-%d'))
        current += timedelta(days=1)
    df = pd.DataFrame({'Representativt dygn': dates, 'Lufttemperatur': NewData})
    df.to_csv('Predicted2025.csv', sep=';', index=False)

if __name__ == '__main__':
    WriteToCSV()
    
