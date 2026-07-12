''' 
1. Customer Feedback Validation System
A company collects customer ratings through a console application. Users sometimes enter
text instead of numbers, leave the value blank, or enter ratings outside the allowed range (1-5).
Task:
Create a program that:
• Accepts a customer rating.
• Ensures the rating is between 1 and 5.
• Displays appropriate error messages for invalid inputs.
• Continues asking until a valid rating is entered.
'''
while True:
  try:
    rating = int(input("Enter a rating(1-5): "))
    if rating>5 or rating<1:
      print("Invalid Rating")
    else:
      print("The customer rating for company is: ",rating)
      break
  except ValueError:
    print("The invalid input for Rating")
  except Exception as e:
    print("There is some error: ",e)