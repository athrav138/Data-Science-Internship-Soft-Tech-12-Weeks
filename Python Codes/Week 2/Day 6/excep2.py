a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

l1 = [1, 2, 3, 4, 5]

try:
    print(l1[59])          # IndexError
    print("Division =", a / b)
    print(l1[59])

except ZeroDivisionError:
    print("Divide by zero not possible")

except IndexError as e:
    print(e)

except Exception as e:
    print(e)

finally:
    print("All done")

print("end")