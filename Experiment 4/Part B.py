import os
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv("Exp 4 - Part B.csv", header = 1)

data["dis_m"] = data["distance"]/100
data["length_m"] = data["length"]/100

data["angle"] = [math.degrees(math.atan(i)) for i in data["length_m"]/data["dis_m"]]
data["sin_angle"] = [math.sin(math.radians(i)) for i in data["angle"]]

slope_intercept = np.polyfit(data["sin_angle"], data["order"]*(5.29*(10**-7)), 1)

fit = slope_intercept[0] * data["sin_angle"] + slope_intercept[1]

print(slope_intercept[0])

plt.scatter(data["sin_angle"], data["order"]*(5.29*(10**-7)), color = "red", label = "Original Data Points")
plt.plot(data["sin_angle"], fit, label = "Fit")
plt.xlabel("sin of angle of deviation")
plt.ylabel("order * wavelength of the source of light")
plt.legend()
plt.show()