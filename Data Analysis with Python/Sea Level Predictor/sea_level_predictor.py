import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots()

    # Create scatter plot

    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    line1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x1 = np.concatenate((df["Year"].values, np.arange(2014, 2051)))
    ax.plot(x1, line1.intercept + line1.slope * x1)
    # Create second line of best fit

    # getting the index of year 2000
    idx_2000 = df[df["Year"].isin([2000])].index[0]
    # fitting the 2nd line
    line2 = linregress(df.iloc[idx_2000:, 0], df.iloc[idx_2000:, 1])
    x2 = np.concatenate((df["Year"].values[idx_2000:], np.arange(2014, 2051)))
    ax.plot(x2, line2.intercept + line2.slope * x2, color="orange")

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
