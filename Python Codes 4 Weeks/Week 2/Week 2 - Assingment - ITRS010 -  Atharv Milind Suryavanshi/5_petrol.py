'''
5. Fuel Price Revision Notice
A fuel company decides to increase fuel prices by ₹3.50 per litre at all stations.
Data:
prices = [96.5, 97.2, 95.8, 98.1, 96.9]
Task:
• Increase all prices by ₹3.50 using a single operation.
• Display old prices and revised prices.
• Calculate the difference for each station.
• Calculate the average revised fuel price. 
'''

import numpy as np 

prices = [96.5, 97.2, 95.8, 98.1, 96.9]

prices_data = np.array(prices)
print("Prices of petrol: ",prices_data)

# • Increase all prices by ₹3.50 using a single operation.
increase = 3.50
prices_data += 3.50
print("Prices of petrol after increase: ",prices_data)

# • Display old prices and revised prices.
old_prices = prices_data - 3.50

print("Prices of petrol old: ",old_prices)
print("Prices of petrol revised: ",prices_data)

# • Calculate the difference for each station.
diff = prices_data - old_prices
print("The difference for each station: ",diff)

# • Calculate the average revised fuel price. 
print("The average of revised fuel price: ",np.mean(prices_data))
