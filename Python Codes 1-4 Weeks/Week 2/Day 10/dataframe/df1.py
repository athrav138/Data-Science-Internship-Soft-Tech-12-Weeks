import pandas as pd

dict = {
  "Name": ["Atharv","Aps","Suyash"],
  "Age" :[18,17,19],
  "Percent":[94.82,89,98.3]
}

df = pd.DataFrame(dict)

print(df)