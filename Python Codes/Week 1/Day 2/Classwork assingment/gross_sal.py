import sys

basic_sal = int(input("Enter basic salary: "))

gross_sal = 0 
if basic_sal<=10000  and basic_sal>0:
  hra = basic_sal * (20/100)
  da = basic_sal * (80/100)
  gross_sal = basic_sal+hra+da

elif basic_sal<=20000 and basic_sal>10000:
  hra = basic_sal * (25/100)
  da = basic_sal * (90/100)
  gross_sal = basic_sal+hra+da

elif basic_sal>20000  :
  hra = basic_sal * (30/100)
  da = basic_sal * (95/100)
  gross_sal = basic_sal+hra+da

else :
  print("Invalid salry amount")
  sys.exit(0)

print(f"Basic salary is {basic_sal} and gross salary is {gross_sal}")