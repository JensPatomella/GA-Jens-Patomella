import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def data():
    df = pd.read_csv("smhi-opendata-1.csv", on_bad_lines='skip', sep=';', usecols=['Lufttemperatur', 'Representativt dygn'])
    return df.values

def predicted(year):
    previous = data()
    prediction = []
    for k in range(1,13):
        for l in range(1,32):
            temps = []
            years = []
            c = 0
            for i in previous:
                if i[0].endswith("{k}-{l}"):
                    temp = float(i[1])
                    year_val = 0 + c
                    c += 1
                    years.append(year_val)
                    temps.append(temp)
                    index = np.where(previous == i[0])
                    previous = np.delete(previous, index[0] , 0)
            X = np.array(years).reshape(-1, 1)
            y = np.array(temps)
            model = LinearRegression()
            model.fit(X, y)
            prediction.append(model.predict([[year]])[0])
    return prediction

print(predicted(28))
