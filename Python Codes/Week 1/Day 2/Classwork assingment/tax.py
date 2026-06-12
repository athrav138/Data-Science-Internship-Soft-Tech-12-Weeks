annual_income = int(input("Enter anaul income: "))


if annual_income<=250000 and annual_income>0 :
  print(f"No tax for {annual_income} annual income")

elif annual_income>500000 and annual_income<=1000000 :
  tax = annual_income * (20/100)
  print(f"{tax} tax for {annual_income} annual income")

elif annual_income>1000000:
  tax = annual_income * (30/100)
  print(f"{tax} tax for {annual_income} annual income")

else :
  print("Invalid amount")