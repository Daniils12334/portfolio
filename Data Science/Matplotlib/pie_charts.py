import numpy as np
import matplotlib.pyplot as plt

langs = ["Python", "C++", "Java", "C#", "Kotlin"]
votes = [50,24,14,6,2]
explodes = [0,0,0.1,0,0]

plt.pie(votes, labels=langs, explode=explodes,
        autopct="%.2f%%", startangle=40, pctdistance=1.4)
plt.show()