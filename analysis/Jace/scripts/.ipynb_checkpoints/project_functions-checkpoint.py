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
