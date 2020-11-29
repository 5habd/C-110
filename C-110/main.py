import csv
import plotly.figure_factory as ff 
import pandas as pd 
import statistics 
import plotly.graph_objects as go
import random
df=pd.read_csv("data.csv")

data=df["temp"].tolist()

population_mean=statistics.mean(data)

fig=ff.create_distplot([data],["temp"],show_hist=False)

datamean=statistics.mean(data)

datamedian=statistics.median(data)

datamode=statistics.mode(data)

print("mean,median,mode of temprature is: {},{},{}".format(datamean,datamedian,datamode))

datastd = statistics.stdev(data)

print(datastd)


def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


def show_hist(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temprature"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()


def setup():
    meanlist=[]
    for i in range( 0,1000 ):
        setofmeans=randomsetofmean(100)
        meanlist.append(setofmeans)
    show_hist(meanlist)
    mean=statistics.mean(meanlist)
    print("mean of sampling distribution",mean )
setup()


def standarddeviation():
    meanlist=[]
    for i in range( 0,1000 ):
        setofmeans=randomsetofmean(100)
        meanlist.append(setofmeans)
    std_dev=statistics.stdev(meanlist)
    print("standard deviation of sampling",std_dev)
standarddeviation()