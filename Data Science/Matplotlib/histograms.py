import matplotlib.pyplot as plt
import numpy as np

ages = np.random.normal(20,1.5,1000)
print(ages)


plt.hist(ages,
        #  bins=[ages.min(), 18, 21, ages.max()])
        bins = 20)
plt.show()