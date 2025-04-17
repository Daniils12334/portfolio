import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
# https://matplotlib.org/stable/users/explain/customizing.html own stylesheets

x1, y1 = np.random.random(100), np.random.random(100)
x2, y2 = np.arange(100), np.random.random(100)

plt.figure(1)
plt.scatter(x1,y1)

plt.figure(2)
plt.plot(x2,y2)

plt.show()