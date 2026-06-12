def add(*n):
  sum = 0
  for i in n:
    sum += i
  
  print("Sum is:",sum)

add(1,2,2,4,5)


def sub(*n):
  sub= n[0]
  for i in range(1,len(n)):
    sub -= n[i]
  
  print("Sub is:",sub)

sub(15,4,-34)
