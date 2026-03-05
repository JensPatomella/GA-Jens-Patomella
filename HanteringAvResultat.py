import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


def dataP():
    df = pd.read_csv('Predicted2025New.csv', on_bad_lines='skip', sep=';', usecols=['Lufttemperatur'])
    return df.values

def dataR():
    df = pd.read_csv('RealVals2025.csv', on_bad_lines='skip', sep=';', usecols=['Lufttemperatur'])
    return df.values

def MeanAbsDifference():
    pred = dataP()
    real = dataR()
    totaldiff = 0
    for i in range(0,365):
        totaldiff += abs(pred[i]-real[i])
    totaldiff = totaldiff/365
    return totaldiff

def MedianAbsDifference():
    pred = dataP()
    real = dataR()
    listdiff = []
    for i in range(0,365):
        listdiff.append(abs(pred[i]-real[i]))
    listdiff = sorted(listdiff)
    median = listdiff[182]
    return median, listdiff[0], listdiff[364]


def ListDifference():
    pred = dataP()
    real = dataR()
    listdiff = []
    for i in range(0,365):
        listdiff.append(pred[i]-real[i])
    return listdiff

def ListAbsDifference():
    pred = dataP()
    real = dataR()
    listdiff = []
    for i in range(0,365):
        listdiff.append(abs(pred[i]-real[i]))
    return listdiff


print(ListDifference())
print(MeanAbsDifference())
print(MedianAbsDifference())

def R2():
    df = pd.read_csv('Predicted2025New.csv', on_bad_lines='skip', sep=';', usecols=['R2'])
    return df.values

def R2Mean():
    tot = 0
    for i in R2():
        tot += i[0]
    tot = tot/365
    return tot

def R2Median():
    list = R2()
    list = sorted(list)
    return list[182], list[0], list[364]

print(R2Mean())
print(R2Median())

def draw(funk, min, max):
    a = funk
    b = []
    for i in a:
        b.append(float(i))
    x1 = np.array(b, dtype=np.float64)
    kde1 = stats.gaussian_kde(x1)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x1, np.zeros(x1.shape), 'b+', ms=20)  # rug plot
    x_eval = np.linspace(min, max, num=365)#från -10 till 30 grader
    ax.plot(x_eval, kde1(x_eval), 'k-', label="Scott's Rule")
    plt.show()

draw(ListDifference(), -20, 20)
draw(R2(), -0.2, 0.4)

