#Imports
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import numpy as np

#Reading in the csv file containing the data. 
df = pd.read_csv("natwest_data.csv")

#Creating figure and subplots.
fix, ax = plt.subplots()

#Using twinx to plot both mean temp and malaria deaths on same plot.
ax.plot(df["year"],
        df["mean_temp"],
        color="red",
        marker="o",
        markersize=3
        )

#Setting up mean temp plot.
ax.set_xlabel("Year", fontsize = 14)
ax.set_ylabel("The Mean Temperature",
              color="red",
              fontsize=14)

ax2 = ax.twinx()

#Setting up malaira deaths plot
ax2.plot(df["year"],
         df["malaria_deaths"],
         color="blue",
         marker="o",
         markersize=3
        )

ax2.set_ylabel("Malaria Deaths", color="blue", fontsize=14)

#Some cleaning up of the graph and ensuring x axis has integer years.
ax.margins(0.05)
ax.axis("tight")
fix.tight_layout
ax.xaxis.set_major_locator(tic.MaxNLocator(integer=True))

#Plotting graph
plt.show()