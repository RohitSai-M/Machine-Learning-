import csv
import os

# Create a sample enjoysport.csv file if it does not exist
if not os.path.exists('enjoysport.csv'):
    sample_data = [
        ['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'],
        ['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'],
        ['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no'],
        ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes']
    ]
    with open('enjoysport.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)

a = []
with open('enjoysport.csv', 'r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)
print("\n The total number of training instances are : ",len(a))
num_attribute = len(a[0])-1
print("\n The initial hypothesis is : ")
hypothesis = ['0']*num_attribute
print(hypothesis)
for i in range(0, len(a)):
 if a[i][num_attribute] == 'yes':
  for j in range(0, num_attribute):
      if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
          hypothesis[j] = a[i][j]
      else:
          hypothesis[j] = '?'
 print("\n The hypothesis for the training instance {} is :\n" .format(i+1),hypothesis)
print("\n The Maximally specific hypothesis for the training instance is ")
print(hypothesis)
Import pandas as pd
from IPython.display import display, HTML

# Attributes from the EnjoySport concept
attributes = ['Sky', 'AirTemp', 'Humidity', 'Wind', 'Water', 'Forecast']

# Create a DataFrame to beautifully show the final hypothesis
df_hypothesis = pd.DataFrame([hypothesis], columns=attributes)

print("\n=== Final Maximally Specific Hypothesis ===\n")
display(df_hypothesis)
