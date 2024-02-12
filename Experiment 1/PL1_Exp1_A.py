# Part A

import numpy as np
import matplotlib.pyplot as plt

# mass of the blob used in the simple pendulum
mass = np.array([34, 27, 25])

# time period (raw data collected) in seconds

tp = np.array([[9.15, 9.25, 9.2], [9.25, 9.15, 9.25], [9.19, 9.31, 9.31]])/10.0

atp = np.round(np.average(tp, axis = 0), 2)

approx = np.polyfit(mass, atp, 1)

slope = approx[0]
intercept = approx[1]

ftp = slope*mass+intercept

r_err = 0.001

plt.scatter(mass, atp, color = "red", label = "Data Points")
plt.plot(mass, ftp,  color = "blue", label = "Fit")
plt.ylabel("Time Period (seconds)")
plt.xlabel("Mass (g)")
plt.ylim([0, 2])
plt.xlim([20, 40])
plt.text(22.5,1.5,fr'$y = {np.round(slope,2)}x + {np.round(intercept,2)}$')
plt.errorbar(mass, atp, yerr = r_err, capsize=5, ecolor = "black", label = "error", linestyle = "None")
plt.legend()
plt.show() 
