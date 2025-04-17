import numpy as np
import matplotlib.pyplot as plt

stock_a = [100,102,99,101,101,100,102]
stock_b = [90,95,102,104,105,103,109]
stock_c = [110,125,102,104,105,90,95]
votes = [10,2,5,1,22]
people = ["A","B","C","D","E"]

plt.figure(1)
plt.plot(stock_a, label = "Company 1")
plt.plot(stock_b, label = "Company 2")
plt.plot(stock_c, label = "Company 3")
plt.legend(loc="lower center")

plt.figure(2)
plt.pie(votes, labels = None)
plt.legend(labels = people)

plt.show()