'''
3. Warehouse Inventory Investigation
A warehouse manager suspects that some storage racks contain significantly more products than others.
Data:
inventory = [120, 85, 150, 60, 95, 180]
Task:
• Store the data in an appropriate numerical structure.
• Find the total stock available.
• Find the highest and lowest stock quantity.
• Calculate the average stock.
• Display all stock quantities greater than 100.
'''

import numpy as np

# • Store the data in an appropriate numerical structure.
inventory = [120, 85, 150, 60, 95, 180]
data_inventory = np.array(inventory)
print("Data Inventory : ",data_inventory)
print()

# • Find the total stock available.
print("The stock available is: ",np.sum(data_inventory))
print()

# • Find the highest and lowest stock quantity.
print("The highest  stock available: ",np.max(data_inventory))
print()

print("The lowest  stock available: ",np.min(data_inventory))
print()


# • Calculate the average stock.
print("The average of stockss: ",np.mean(data_inventory))
print()


# • Display all stock quantities greater than 100.
print("The all stock quantites greater than 100: ",data_inventory[data_inventory>100])