# Part B

import matplotlib.pyplot as plt
import numpy as np 

# length of the SP (in cm -- being converted into meters here)
length = np.array([53.4, 48.4, 43.4, 38.4, 33.4, 28.4, 23.4, 20.9, 18.4, 15.4])/100.0
#print("length", length)

# time period (the raw data collected) in seconds
tp = np.array([[14.71, 14.04, 13.21, 12.37, 11.59, 10.71, 9.72, 9.13, 8.66, 7.84], [14.72, 14.16, 13.25, 12.41, 11.62, 10.72, 9.72, 9.15, 8.60, 7.84], [14.63, 14.03, 13.09, 12.44, 11.59, 10.69, 9.69, 9.19, 8.59, 7.87]])/10.0

# average time period and squaring it further for plotting
atp = np.square(np.average(tp, axis=0))

#print("average time period: ", atp)

# getting an approximation of the original data by using polyfit
approx = np.polyfit(length, atp, 1)

#print("approx: ", approx)

# assigning the values of slope and intercept
slope = approx[0]
intercept = approx[1]

#print("slope", slope)
#print("intercept", intercept)

# final value of time period to be used for plotting the grapj
ftp = (slope * length) + intercept

print(slope)
print(intercept)

# g in m/s**2, apparently
g = 4* np.pi ** 2 / slope

print("g:", g)


plt.scatter(length, atp, color = "red", label = "Data Points")
plt.plot(length, ftp, color = "blue", label = "Fit")
plt.ylim([0.5,2.5])
plt.ylabel("Time Period (second square)")
plt.xlabel("Length (m)")
plt.legend()
plt.show()  


'''
z = []
for l in length: 
    t = (2*3.14*(l/9.8)**(1/2))
    z.append(t)
print(z)

difference = np.abs(atp - z)
print(difference)
'''