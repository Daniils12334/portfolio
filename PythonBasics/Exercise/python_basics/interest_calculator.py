principle, time, rate = 0,0,0

while principle <= 0:
    principle = float(input("enter the principle amount"))
    if principle <= 0:
        print("principle cant be less then zero")

while rate <= 0:
    rate = float(input("enter the rate of interest"))
    if rate <= 0:
        print("rate cant be less then zero")

while time <= 0:
    time = float(input("enter the time in years"))
    if time <= 0:
        print("time cant be less then zero")

total = principle * pow((1+rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
print(principle, " ", rate, " ", time)
