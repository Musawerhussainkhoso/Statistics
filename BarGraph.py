#create frequency table

import pandas as pd

marks = [60, 70, 60, 80, 70, 60, 90, 80, 70, 60]

frequency_table = pd.Series(marks).value_counts().sort_index()
print("Frequency Table:")
print(frequency_table)
