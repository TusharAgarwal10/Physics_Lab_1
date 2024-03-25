import os
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv("Part A - Data.csv").iloc[4:, :]
data1["l1-l2"] = data1["l1 (left)"] - data1["l2 (left)"]
data1["l1+l2"] = data1["l1 (left)"] + data1["l2 (left)"]

slope_intercept1 = np.polyfit(data1["l1-l2"], data1["Resistance"], 1)
fit1 = slope_intercept1[0] * data1["l1-l2"] + slope_intercept1[1]

r_err1 = np.round(0.3986957905, 4)

data2 = pd.read_csv("Part B - Data.csv")
data2["l1-l2"] = data2["l1 (left)"] - data2["l2 (left)"]
data2["l1+l2"] = data2["l1 (left)"] + data2["l2 (left)"]

slope_intercept2 = np.polyfit(data2["l1-l2"], data2["Resistance"], 1)
fit2 = slope_intercept2[0] * data2["l1-l2"] + slope_intercept2[1]

r_err2 = np.round(0.4949747468, 4)

plt.scatter(data1["l1-l2"], data1["Resistance"], color = "red", label = "Original data1 Points")
plt.plot(data1["l1-l2"], fit1, label = "fit1")
plt.text(65, 1.65, fr'$y_{1} = {np.round(slope_intercept1[0],4)}x_{1} + ({np.round(slope_intercept1[1],4)})$')
plt.errorbar(data1["l1-l2"], data1["Resistance"], xerr = r_err1, capsize=5, ecolor = "black", linestyle = "None")

plt.xlabel("Balance Length Difference (cm)")
plt.ylabel("Resistance (omega)")
plt.legend()
plt.show()

