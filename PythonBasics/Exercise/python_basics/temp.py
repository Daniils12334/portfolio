temp = 20 
is_raining = False

if temp > 35 or temp < -10 or is_raining:
    print("The weather is extreme")
else:
    print("the weather is normal")

print ("Postive" if temp > 0 else "Negative")