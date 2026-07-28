f = open("article.txt", "r")

lines = f.readlines()
a_count = 0
an_count = 0
the_count = 0

for line in lines:
    words = line.split()
    for word in words:
        if word.lower()=="a":
            a_count = a_count + 1
        elif word.lower()=="an":
            an_count = an_count + 1
        elif word.lower()=="the":
            the_count = the_count + 1

print(f"Count of 'a': {a_count}")
print(f"Count of 'an': {an_count}")
print(f"Count of 'the': {the_count}")