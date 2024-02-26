import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C://Users//ASUS//Documents//Programming//College Projects//Physics Lab 1//Exp 3//C-A_Data.csv")

xaxis = np.array(df["Voltage (V)"])
yaxis = np.array(df["Current (A)"])

print(df)
fitting = np.polyfit(xaxis[7:], yaxis[7:], 1)

slope = fitting[0]
intercept = fitting[1]

y = slope*xaxis + intercept

print(1/slope)

plt.scatter(xaxis, yaxis, color = "red", label = "Data Points")
plt.plot(xaxis, y, color = "blue", label = "Resistor Fit")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.title("C-A connection")
plt.legend()
plt.show()