'''
7. Smart Factory Temperature Monitoring
Temperature sensors installed in different production units report hourly temperatures.
Data:
temperatures = [28.5, 30.2, 29.8, 31.1, 27.9, 30.5, 29.0]
Task:
• Store the temperature readings in a suitable analytical structure.
• Calculate average temperature.
• Find the highest and lowest temperatures.
• Display temperatures above the average.
• Generate a summary table containing all readings. 
'''
import numpy as np
import pandas as pd

temperatures = [28.5, 30.2, 29.8, 31.1, 27.9, 30.5, 29.0]

# • Store the temperature readings in a suitable analytical structure.
temp_data = np.array(temperatures)
print("Temperature data: ",temp_data)

# • Calculate average temperature.
avg = np.mean(temp_data)
print("The average of temperature: ",avg)

# • Find the highest and lowest temperatures.
print("The highest temperature: ",np.max(temp_data))
print("The lowest temperature: ",np.min(temp_data))

#  • Display temperatures above the average.
print("The temperatures above the average: ",temp_data[temp_data>avg])

# • Generate a summary table containing all readings. 
df = pd.DataFrame(temp_data)
print("The summary table conataining all readings: \n",df.describe())

