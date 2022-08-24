import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    ## you may have to write the full address of the file to be opened
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    plt.scatter(x, y, c = 'grey', s = 10, label = "CSIRO Adjusted Sea Level")

    # Create first line of best fit
    stats = linregress(x, y)
    a = stats.slope
    b = stats.intercept
    x1 = range(1880, 2051)
    plt.plot(x1, a * x1 + b, color = "blue", label = "1880-2050 prediction")

    # Create second line of best fit
    df2k = df[df["Year"] >= 2000]
    x = df2k["Year"]
    y = df2k["CSIRO Adjusted Sea Level"]
    stats = linregress(x, y)
    a = stats.slope
    b = stats.intercept
    x2 = range(2000, 2051)
    plt.plot(x2, a * x2 + b, color = "red", label = "2000-2050 prediction")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    ## To make the graph more understandable, 
    ## I wanted to add a legend, 
    ## but it turned out that this would not work in the standard way, 
    ## because duplicates appear. 
    ## The answer was found:

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc = "upper left", title = "Sea level", prop = {"size": 7})

    # Save plot and return data for testing (DO NOT MODIFY)
    ## you may have to change the save location of the png, because not all devices save correctly
    plt.savefig('sea_level_plot.png')
    return plt.gca()