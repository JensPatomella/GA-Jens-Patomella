from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

def data(filename):
    df = pd.read_csv(filename, on_bad_lines='skip', sep=';', usecols=['Lufttemperatur', 'Representativt dygn'])
    return df.values

def draw(filename):
    a = data(filename)
    b = []
    for i in a:
        b.append(float(i[1]))
    x1 = np.array(b, dtype=np.float64)
    kde1 = stats.gaussian_kde(x1)
    kde2 = stats.gaussian_kde(x1, bw_method='silverman')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x1, np.zeros(x1.shape), 'b+', ms=20)  # rug plot
    x_eval = np.linspace(-10, 30, num=200)#från -10 till 30 grader
    ax.plot(x_eval, kde1(x_eval), 'k-', label="Scott's Rule")
    ax.plot(x_eval, kde2(x_eval), 'r-', label="Silverman's Rule")
    plt.show()

draw("predicted2025.csv")

