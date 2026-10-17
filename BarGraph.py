#create frequency table

import pandas as pd

marks = [60, 70, 60, 80, 70, 60, 90, 80, 70, 60]

frequency_table = pd.Series(marks).value_counts().sort_index()
print("Frequency Table:")
print(frequency_table)


#You can create the frequency table and bar graph together
import matplotlib.pyplot as plt

marks = [60, 70, 60, 80, 70, 60, 90, 80, 70, 60]

frequency = pd.Series(marks).value_counts().sort_index()

frequency.plot(kind="bar")

plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Frequency Distribution of Marks")
plt.show()


print("..................................................................................................")

ages = [12, 14, 15, 17, 18, 19, 21, 22, 24, 26]

# Ungrouped frequency
print("Ungrouped:")
print(pd.Series(ages).value_counts().sort_index())

# Grouped frequency
bins = [10, 15, 20, 25, 30]

print("\nGrouped:")
print(pd.cut(ages, bins=bins, right=False).value_counts().sort_index())


