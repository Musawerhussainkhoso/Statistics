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

