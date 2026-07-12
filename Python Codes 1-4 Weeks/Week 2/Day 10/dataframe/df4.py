import pandas as pd

dict = {
  "Name":["Atharv","Aps","Shree","Om","Anuj"],
  "Age":[12,34,45,56,67],
  "Marks":[98.23,86.5,56,67,56.4]
}

df = pd.DataFrame(dict)


print(df[df["Marks"]>60])