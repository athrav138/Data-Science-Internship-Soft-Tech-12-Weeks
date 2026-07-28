a=10
b=0

try:
    c = a/b
    print(c)
    
except Exception as e:
    print(f"Error:{e}")
    
finally:
    print("finally executed")
    
    
print("next code")