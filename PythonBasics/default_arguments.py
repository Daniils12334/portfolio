# default arguments = Arguments that take a default value if no argument value is passed during the function call.
import time

def net_price(price, discount = 0, tax = 0.05):
    return price * (1-discount) * (1+tax)

def count(end, start = 0):
    for x in range(start, end):
        print(x)
        time.sleep(1)
    print("Done!")

count(30,15)