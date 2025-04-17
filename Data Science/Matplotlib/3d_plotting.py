import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

ax = plt.axes(projection = "3d")

x = np.arange(0, 50, 0.1)
y = np.arange(0,50,0.1)
z = np.cos(x)

q = np.random.random(100)
w = np.random.random(100)
e = np.random.random(100)

plt.figure(1)
ax.scatter(x,y,z)
ax.set_title("3D plot")
ax.set_xlabel("TEST")

plt.figure(2)
zx = plt.axes(projection = "3d")
zx.scatter(q,w,e)
zx.set_title("3D plot")
zx.set_xlabel("TEST")

plt.show()

