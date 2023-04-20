#Imports
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr

#Reading in the csv file containing the data. 
df = pd.read_csv("natwest_data.csv")

#Exctract the correctn years and the change in deaths and temp.
change_in_temp = []
change_in_deaths = []
years = []

for i in range(1,len(df["malaria_deaths"])-1):
    change_in_deaths.append(df["malaria_deaths"][i] - df["malaria_deaths"][i-1])
    change_in_temp.append(df["mean_temp"][i] - df["mean_temp"][i-1])
    years.append(df["year"][i])

#Creating figure and subplots.
fig, axs = plt.subplots(2)

#Using twinx to plot both change in mean temp and change in malaria deaths on same plot.
axs[0].plot(years,
        change_in_temp,
        color="red",
        marker="o",
        markersize=3
        )

#Setting up change in mean temp plot.
axs[0].set_xlabel("Year", fontsize = 14)
axs[0].set_ylabel("Change In Mean Temperature",
              color="red",
              fontsize=14)

ax2 = axs[0].twinx()

#Setting up change in malaira deaths plot.
ax2.plot(years,
         change_in_deaths,
         color="blue",
         marker="o",
         markersize=3
        )

ax2.set_ylabel("Change In Malaria Deaths", color="blue", fontsize=14)

#Some cleaning up of the graph and ensuring x axis has integer years.
axs[0].margins(0.05)
axs[0].axis("tight")
fig.tight_layout
axs[0].xaxis.set_major_locator(tic.MaxNLocator(integer=True))
axs[0].grid("on")
axs[0].set_title("The changes in Malaria deaths and Mean temperature in Nigeria through 2001 - 2019")

#plotting change in deaths against change in temp.
axs[1].plot(
    change_in_deaths,
    change_in_temp,
    "o",
    color="blue"
)

#Adding some axis labels.
axs[1].set_xlabel("Change In Malaria Deaths", fontsize=14)
axs[1].set_ylabel("Change In Mean Temperature", fontsize=14)
axs[1].grid("on")
axs[1].set_title("The changes in Malaria deaths against the changes in Mean temperature in Nigeria through 2001 - 2019")

#creating function for trendline.
z = np.polyfit(change_in_deaths, change_in_temp, 1)
p = np.poly1d(z)

axs[1].plot(
    change_in_deaths,
    p(change_in_deaths),
    color="blue",
    linewidth=1)

#Calculating spearmans and pearsons correlation coefficient on the data.
pcorr, _ = pearsonr(change_in_deaths, change_in_temp)
scorr, _ = spearmanr(change_in_deaths, change_in_temp)

#Plotting graph
plt.show()