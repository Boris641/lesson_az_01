import pandas as pd

df = pd.read_csv('dz.csv')

print(df.info)
print(df[['Salary','City']])

group = df.groupby('City')['Salary'].mean()
print(group)