import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C://Users//ASUS//Documents//Programming//Python//Physics Lab 1//Exp 2//Exp2 - P1.csv")

mass = np.array(df["Mass of bobs (g)"])
elength = (np.array(df["Extended Length (cm)"]) - 76.7)

average = np.polyfit(mass, elength, 1)
print(average)

slope = average[0]
intercept = average[1]

y = slope *  mass + intercept

k = 9.81/np.round(slope, 2)/10
print(k)

plt.scatter(mass, elength, color = "red", label = "Data Points")
plt.plot(mass, y, label = "Fit")
plt.xlabel("Mass (g)")
plt.ylabel("Extended Length (cm)")
plt.legend()
plt.text(10,40,fr'$y = {np.round(slope,2)}x + ({np.round(intercept,2)})$')
plt.show()
