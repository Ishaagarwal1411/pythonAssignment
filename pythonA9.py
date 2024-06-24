import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data
months = np.arange(12) + 1
max_temps = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
min_temps = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])

# Define a periodic function (sine function) with parameters: amplitude, mean, and period
def periodic_func(x, amplitude, mean, period):
    return amplitude * np.sin((2 * np.pi / period) * (x - mean))

# Fit the maximum temperature data
popt_max, pcov_max = curve_fit(periodic_func, months, max_temps, bounds=([20, 0, 0], [50, 12, 12]))

# Fit the minimum temperature data
popt_min, pcov_min = curve_fit(periodic_func, months, min_temps, bounds=([10, 0, 0], [30, 12, 12]))

# Plotting
plt.figure(figsize=(10, 6))

# Plot the max temperature data and the fitted curve
plt.plot(months, max_temps, 'ro', label='Max Temp Data')
plt.plot(months, periodic_func(months, *popt_max), 'r-', label='Max Temp Fit: Amplitude={}, Mean={}, Period={}'.format(*popt_max))

# Plot the min temperature data and the fitted curve
plt.plot(months, min_temps, 'bo', label='Min Temp Data')
plt.plot(months, periodic_func(months, *popt_min), 'b-', label='Min Temp Fit: Amplitude={}, Mean={}, Period={}'.format(*popt_min))

plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.title('Seasonal Variation of Temperatures')
plt.xticks(months)
plt.legend()
plt.grid(True)
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Read the Titanic dataset
url = "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv"
titanic = pd.read_csv(url)

# Data cleaning (if needed)
# titanic.dropna(inplace=True)  # Example of dropping rows with missing values

# Task 1: Pie chart for male/female proportion
gender_counts = titanic['sex'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['skyblue', 'lightcoral'])
plt.title('Male/Female Proportion in Titanic Dataset')
plt.show()

# Task 2: Scatter plot for Fare vs Age, colored by gender
plt.figure(figsize=(10, 6))
plt.scatter(titanic[titanic['sex'] == 'male']['age'], titanic[titanic['sex'] == 'male']['fare'], label='Male', color='skyblue', alpha=0.6)
plt.scatter(titanic[titanic['sex'] == 'female']['age'], titanic[titanic['sex'] == 'female']['fare'], label='Female', color='lightcoral', alpha=0.6)
plt.xlabel('Age')
plt.ylabel('Fare Paid')
plt.title('Fare Paid vs Age, Colored by Gender')
plt.legend()
plt.grid(True)
plt.show()
