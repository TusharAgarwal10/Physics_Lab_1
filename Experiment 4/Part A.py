import os
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv("Exp 4 - Part A.csv", header = 1)

data["dis_m"] = data["distance"]/100
data["length_m"] = data["length"]/100
data["space_m"] = data["spacing"]/1000

data["angle"] = [math.degrees(math.atan(i)) for i in data["length_m"]/data["dis_m"]]
data["sin_angle"] = [math.sin(math.radians(i)) for i in data["angle"]]

slope_intercept = np.polyfit(data["order"]/data["space_m"], data["sin_angle"], 1)

fit = slope_intercept[0] * data["order"]/data["space_m"] + slope_intercept[1]

print(slope_intercept[0])

plt.scatter(data["order"]/data["space_m"], data["sin_angle"], color = "red", label = "Original Data Points")
plt.plot(data["order"]/data["space_m"], fit, label = "Fit")
plt.xlabel("order/grating spacing")
plt.ylabel("sin of angle of deviation")
plt.errorbar(data["order"]/data["space_m"], data["sin_angle"], yerr = 0.001, capsize=5, ecolor = "black", label = "Least Count Error", linestyle = "None")
plt.legend()
plt.show()

print(data)


