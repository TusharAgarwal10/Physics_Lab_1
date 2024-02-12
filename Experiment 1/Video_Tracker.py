import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  

df = pd.read_csv("video_tracker_data.csv", header=1)


time = np.array(df["t"][1800:])
xaxis = np.array(df["x"][1800:])
yaxis = np.array(df["y"][1800:])


# 3D representation
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot3D(time, xaxis, yaxis, color = "red")
ax.set_xlabel("Time")
ax.set_ylabel("x_axis")
ax.set_zlabel("y_axis")
plt.show()


# 2D representation
'''plt.plot(xaxis, yaxis)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
plt.grid()
plt.xlim(-10,10)
plt.ylim(-10,10 )
'''