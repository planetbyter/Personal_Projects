import numpy as np
import datetime as datetime
import pandas as pd
import matplotlib.pyplot as plt

# Weekly Inbound Email Volume
num1 = np.array([32763])
num2 = np.array([45718])
num3 = np.array([38103])
num4 = np.array([53745])

print ("1st array : ", num1)
print("2nd Array: ", num2)
print("3rd Array: ", num3)
print("4th Array: ", num4)

added_arrays1 = np.add(num1, num2)
added_arrays2 = np.add(num3, num4)
total_number = np.add(added_arrays1, added_arrays2)
print("Added Array: ", total_number)

if total_number < 43000:
    print("This number is in the the acceptable bound.")
else:
    print("This number is not within the acceptable bound.")

# Time Series Analysis
z = np.array([datetime.datetime(2021, 2, 26, i, 0) for i in range(24)])
y = np.random.randint(43000, size=z.shape)
plt.plot(z,y)
plt.show()

def variance(total_number):
    # Number of observations
    n = 4
    print("Number of observations: ", n)

    # Mean of the data
    mean = total_number / 4
    print("Mean: ", mean)

    #Square deviations
    deviations = [(total_number - mean) ** 2 for x in total_number]
    print("Deviations: ", deviations)

    #Variance
    variance = sum(deviations) / n
    return variance

variance(total_number)

print(variance(total_number))


