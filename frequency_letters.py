import os
import sys
import time
from collections import Counter
import pandas
import matplotlib.pyplot as plt

start = time.time()
# Path variable contains the first command line argument passed
path = sys.argv[1]

# Check if path exits
if os.path.exists(path):
    print("File exist")

# Read the file
with open(path, 'r') as f:
    file_name_data = f.read()
    file_name_data = file_name_data.lower()

# Convert to a list where each character is an element
character_list = list(file_name_data)

# Get the frequency of each character with Python Counter tool. The variable 'character_counter' is a collection where
# the elements are stored as dictionary keys and their counts are stored as dictionary value
character_counter = Counter(character_list)

# Convert the Counter into Pandas data frame. The option orient='index' create the DataFrame using dictionary keys as
# rows
# The method reset_index() reset the index and a new sequential index is used (whereas the old is added as a column)
df = pandas.DataFrame.from_dict(character_counter, orient='index').reset_index()

df = df.rename(columns={'index': 'letter', 0: 'frequency'})

# The isin() method is used to select rows that have a particular value in the data frame
df = df.loc[df['letter'].isin(
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z'])]

print(df)

# Calculate the relative frequency of each letter
df['rel_freq'] = df['frequency'] / df['frequency'].sum()

# Sort alphabetically
df = df.sort_values('letter')

print(df)

end = time.time()
print(f"Total elapsed time: {end - start}s")

plt.bar(df['letter'], df['frequency'])
plt.title('Letters frequency')
plt.show()
