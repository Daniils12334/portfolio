import matplotlib.pyplot as plt
import numpy as np

years = [2006 + x for x in range (16)]
weights = [80, 83, 84, 85, 86, 84, 99, 110,
           130, 150, 184, 185, 186, 184, 100, 71 ]

plt.plot(years, weights, c = "red", lw = 3, linestyle = ":")
plt.show()
print (years)