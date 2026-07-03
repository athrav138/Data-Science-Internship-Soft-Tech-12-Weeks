
l  = [1,2,3,4,5,0,]
print(list(i for i in l if i>2) )


print(list(filter(None,l)))
print(list(map(lambda x: x*x,l)))
print("even" if 10%2==0 else "Odd")