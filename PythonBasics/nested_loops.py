
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for l in range(rows):
    for m in range(columns):
        print("|", end = "")
    print()