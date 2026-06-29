r = int(input("roll no:"))
p = int(input("physics marks:"))
c = int(input("chemistry marks:"))
m = int(input("maths marks:"))
total = p + c + m
percentage = (total / 300) * 100

f=open("marklist.txt", "w")
f.write("roll no \t physics \t chemistry \t maths \t total \t percentage\n")
f.write("-------------------------------------------------------------\n")
f.write(f"{r} \t {p} \t {c} \t {m} \t {total} \t {percentage}\n")
f.close()
