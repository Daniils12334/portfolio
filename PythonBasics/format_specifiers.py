price1 = 3.14159
price2 = -987.65
price3 = 1234.56

print(f"Price 1 is {price1:.3f}") # 3 decimal places
print(f"Price 2 is {price2:3}") # 3 spaces
print(f"Price 3 is {price3:0100}") # 100 zeros
print(f"Price 3 is {price3:0<100}") # 100 zeros
print(f"Price 3 is {price3:0>100}") # 100 zeros
print(f"Price 3 is {price3:0^100}") # 100 zeros
print(f"Price 3 is {price3:0^100.2f}") # 100 zeros