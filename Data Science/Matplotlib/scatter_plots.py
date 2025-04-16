import matplotlib.pyplot as plt
import numpy as np

X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100

# print(X_data)
# print(Y_data)


plt.scatter(X_data, Y_data, c = "green", s = 100, marker = "*", alpha = 0.3)
plt.show()

