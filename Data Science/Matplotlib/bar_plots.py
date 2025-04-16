import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/home/danbar/Desktop/project_x/Other/health_activity_data.csv')

sleep_by_age = df.groupby('Age')['Hours_of_Sleep'].mean()

plt.figure(figsize=(12, 6))
plt.bar(sleep_by_age.index, sleep_by_age.values, color='skyblue')
plt.xlabel('Age')
plt.ylabel('Mean_Hours_of_Sleep')
plt.title('Middle Sleep Hours')
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
