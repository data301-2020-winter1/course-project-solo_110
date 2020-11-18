import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load(path):
    df = pd.read_csv(path)
    dates = pd.to_datetime(df['Date'])
    converted = dates.dt.date
    df.insert(1,'Converted_Date',converted)
    return df


def sort(dataset,column):
    df=dataset.sort_values(by=column,ascending=True)
    return df

def countColumns(dataset):
    count = dataset.shape[1]
    return count

def countRows(dataset):
    count = dataset.shape[0]
    return count

def listColumns(dataset):
    lst = dataset.columns
    for item in lst:
        print(item)

def openCloseBarPlot(dataset):
    avgClose = dataset['Close'].mean()
    avgOpen = dataset['Open'].mean()

    plt.bar("Open",avgOpen,label="Open")
    plt.bar("High",avgClose,label="High")
    plt.legend()
    plt.ylabel("Cost")
    plt.show()
    print("Average opening cost-Average closing cost: $%.2f"%(avgClose-avgOpen))
    
    
def getYearlyDf(dataset):
    yearlydf = dataset[::-1]
    yearlydf = (
        yearlydf.groupby(np.arange(len(yearlydf))//365)
        .mean()
        .round(2)
    )
    return yearlydf

def getMonthlyDf(dataset):
    monthlydf = dataset[::-1]
    monthlydf = (
        monthlydf.groupby(np.arange(len(monthlydf))//30)
        .mean()
        .round(2)
    )
    return monthlydf