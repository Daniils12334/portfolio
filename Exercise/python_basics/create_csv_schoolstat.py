import numpy as np
import pandas as pd

# Settings
n_rows = 1_000_000  # 1 million rows

# Predefined options
names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
countries = ["USA", "Latvia", "Germany", "Japan", "Brazil", "India"]

# Generate data
np.random.seed(0)  # for reproducibility
ages = np.random.randint(18, 70, size=n_rows)
scores = np.random.uniform(0, 100, size=n_rows)
passed = np.random.choice([True, False], size=n_rows)

# For name and country, using random.choices is slower; we'll use numpy here too
name_choices = np.random.choice(names, size=n_rows)
country_choices = np.random.choice(countries, size=n_rows)

# Combine into DataFrame
df = pd.DataFrame({
    "Name": name_choices,
    "Age": ages,
    "Country": country_choices,
    "Score": scores,
    "Passed": passed
})

# Save to CSV
df.to_csv("random_stats.csv", index=False)

print("CSV file with random stats created!")
