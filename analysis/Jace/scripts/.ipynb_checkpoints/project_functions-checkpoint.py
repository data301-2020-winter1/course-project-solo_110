import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def process():
    print("magic is good")
def load(path):
    df = pd.read_csv(path)
    return df


def sort(dataset,column):
    df=dataset.sort_values(by=column,ascending=False)
    return df
