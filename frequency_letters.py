import os
import sys
import time
from collections import Counter

import pandas

import matplotlib.pyplot as plt

start = time.time()
# path variable contains the first command line argument passed
path = sys.argv[1]

# Check if path exits
if os.path.exists(path):
    print("File exist")

with open(path, 'r') as f:
    file_name_data = f.read()
    file_name_data = file_name_data.lower()

# convert to a list where each character is an element
letter_list = list(file_name_data)

# get the frequency of each letter
my_counter = Counter(letter_list)

df = pandas.DataFrame.from_dict(my_counter, orient='index').reset_index()
df = df.rename(columns={'index': 'letter', 0: 'frequency'})

df = df.loc[df['letter'].isin(
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z'])]

df['doc_rel_freq'] = df['frequency']/df['frequency'].sum()
df = df.sort_values('letter')

print(df)
end = time.time()

plt.bar(df['letter'], df['frequency'])
plt.title('Letters frequency')
plt.show()
print(f"Total elapsed time: {end - start}s")
