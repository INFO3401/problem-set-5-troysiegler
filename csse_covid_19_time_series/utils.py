import pandas as pd
import math
import numpy as np
import scipy.stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit
import datetime as dt

def loadAndCleanData(file):
    data = pd.read_csv(file)
    data.fillna(0)
    #print(data)
    return data

# 8

def mergeData(data1, data2, column):
    data = []
    data = data.insert(data2(column))

    data[column] = 0
    data[column] = data1

    return data1

def runANOVA(df, vars):
    model = ols(vars, data=df).fit()
    aov_table = sm.stats.anova_lm(model, typ=2)
    return aov_table

# 10

def plotTimeline(data, time_col, vc):
    sns.lineplot(data=data, x=time_col, y=vc)
    plt.show()

# 12

def plotMultipleTimeLines(data, time_col, vc, cat_col):
    sns.lineplot(data=data, x=time_col, y=vc, hue=cat_col)
    plt.show()
