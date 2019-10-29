import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

def plot_bars(features, target, df):
    for column in df[features].select_dtypes([object, int]).columns.tolist():
        if len(df[column].unique()) <= 5:
            sns.barplot(column, target, data=df)
            plt.title(column)
            plt.ylabel(target)
            plt.show()

def plot_box(features, target, df):
    for discrete in df[features].select_dtypes([object,int]).columns.tolist():
        if df[discrete].nunique() <= 5:
            for continous in df[features].select_dtypes(float).columns.tolist():
                sns.boxplot(discrete,continous,data=df)
                plt.title(continous + ' x ' + discrete)
                plt.ylabel(continous)
                plt.show()

def plot_swarm(features, target, df):
    for discrete in df[features].select_dtypes([object,int]).columns.tolist():
        if df[discrete].nunique() <= 5:
            for continous in df[features].select_dtypes(float).columns.tolist():
                sns.swarmplot(x=continous, y=target, hue=discrete, data=df)
                plt.title(target + ' x ' + continous + ' x ' + discrete)
                plt.ylabel(target)
                plt.xlabel(continous)
                plt.show()