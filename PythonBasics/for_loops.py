credit_card = "4322-1233-4556-2344"

for x in range (0, 10):
    print (x)
for x in reversed(range (0, 10)):
    print (x)
for x in range (0, 10, 5):
    print (x)
for x in credit_card:
    print (f"x equal {x}:")

for x in range (1,21):
    if x == 13:
        continue #break
    else:
        print (x)