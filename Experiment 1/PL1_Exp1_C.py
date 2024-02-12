import matplotlib.pyplot as plt
import numpy as np

angle = np.array([1, 5,10,15,17,20, 25, 90])
time = np.array([[9.37, 9.35, 9.44],[9.31,9.32,9.25],[9.25,9.22,9.25],[9.38,9.38,9.35],[9.41,9.31,9.34],[9.28,9.35,9.28], [9.44, 9.44, 9.38], [10.57, 10.69, 10.53]])/10
avg_time = (np.average(time,axis=1)).round(2)

approx_line = np.polyfit(angle, avg_time, 1)
slope = approx_line[0]
intercept = approx_line[1]

final_tp = slope * angle + intercept

plt.scatter(angle,avg_time, color = "red", label = "Data Points")
plt.plot(angle,final_tp, color = "blue", label = "Fit")
plt.ylabel("Time Period (second)")
plt.xlabel("Angle (degree)")
plt.ylim([0.5,1.5])
plt.xlim([-10,100])
plt.legend()
plt.text(10,1.2,fr'$y = {np.round(slope,2)}x + {np.round(intercept,2)}$')
plt.show()