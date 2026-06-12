import pandas as pd

dict = [
  {"Name":"atharv","Age":38},
  {"Name":"Shree","Age":34}
]

df = pd.DataFrame(dict)

print(df)
print()

print(df["Name"])
print()

print(df.loc[1,"Name"])
print()

print(df.iloc[1])
