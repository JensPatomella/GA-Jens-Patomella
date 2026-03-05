import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
from datetime import datetime, timedelta

def data():
    df = pd.read_csv('smhi-opendata-1.csv', on_bad_lines='skip', sep=';', usecols=['Lufttemperatur', 'Representativt dygn'])
    return df.values

def predicted(year):
    previous = data()
    prediction = []
    R2 = []
    K = []
    M = []
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
            R2.append(model.score(X, y, sample_weight=None))
            K.append(model.coef_)
            M.append(model.intercept_)
        current += timedelta(days=1)
    return prediction, R2, K, M

print(predicted(28))


def WriteToCSV():
    Temp = predicted(28)[0]
    R2 = predicted(28)[1]
    K = predicted(28)[2]
    M = predicted(28)[3]
    start = datetime(2025, 1, 1)
    end = datetime(2025, 12, 31)
    current = start
    dates = []
    while current <= end:
        dates.append(current.strftime('%Y-%m-%d'))
        current += timedelta(days=1)
    df = pd.DataFrame({'Representativt dygn': dates, 'Lufttemperatur': Temp, 'R2': R2, 'K': K, 'M': M})
    df.to_csv('Predicted2025New.csv', sep=';', index=False)

if __name__ == '__main__':
    WriteToCSV()

