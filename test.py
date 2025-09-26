import pandas as pd
import numpy as np

def data():
    df = pd.read_csv("smhi-opendata-1.csv", on_bad_lines='skip', sep=';', usecols=['Lufttemperatur'])
    return df.values

def predicted(): #funkar inte just nu för långsamt tror jag
    temps = []
    pretemps = data()
    for day in range (365):
        for year in range (27):
            c = pretemps[day + (year * 365)]
            temps.append(c)
    return temps

print(len(predicted()))
    
