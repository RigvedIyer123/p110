import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
pmean = statistics.mean(data)
pstddev = statistics.stdev(data)

print("mean:",pmean)
print("standard deviation:", pstddev)

fig = ff.create_distplot([data],["reading_time"],show_hist = False)           

def randomSetOfMean(counter):
    dataset = []
    for i in range (0,counter):
        rIndex = random.randint(0,len(data)-1)
        value  = data[rIndex]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def showFig(meanlist):
    df = meanlist
    fig = ff.create_distplot([df],["avg"],show_hist = False)
    fig.show()

def setup():
    meanlist = []
    for i in range (0,1000):
        setOfMean = randomSetOfMean(100)
        meanlist.append(setOfMean)
    showFig(meanlist)

setup()

def stdev():
    meanlist = []
    for i in range (0,1000):
        setOfMean = randomSetOfMean(100)
        meanlist.append(setOfMean)
    stdev = statistics.stdev(meanlist)
    print("standard deviation of sampling distribution = ", stdev)

stdev()
