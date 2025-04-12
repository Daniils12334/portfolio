import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("random_stats.csv")

# Set seaborn style
sns.set(style="darkgrid")

# Group by Age and calculate average Score
avg_scores_by_age = df.groupby("Age")["Score"].mean().reset_index()

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=avg_scores_by_age, x="Age", y="Score", marker="o")
plt.title("Average Score by Age")
plt.xlabel("Age")
plt.ylabel("Average Score")
plt.grid(True)
plt.show()
