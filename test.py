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
    c = 0
    for i in previous:
        if i[0].endswith("01-01"):
            temp = float(i[1])
            year_val = 0 + c
            c += 1
            years.append(year_val)
            temps.append(temp)
            print(np.where(previous == i[0]))
            #previous = np.delete(previous, (idexet av "i" i "previous") , 0) för att det ska gå fortare desto fler datum som redan är klara

    X = np.array(years).reshape(-1, 1)
    y = np.array(temps)
    model = LinearRegression()
    model.fit(X, y)
    prediction = model.predict([[year]])[0]
    return prediction

print(predicted(28))
