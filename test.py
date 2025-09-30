import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

import pandas as pd
import numpy as np

def data():
    df = pd.read_csv("smhi-opendata-1.csv", on_bad_lines='skip', sep=';', usecols=['Lufttemperatur', 'Representativt dygn'])
    return df.values

def predicted():
    

print((predicted()))
    