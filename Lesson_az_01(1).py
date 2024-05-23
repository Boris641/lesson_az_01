import pandas as pd

df = pd.read_csv('Renewable.csv')
print(df.head())
print(df.info())
print(df.describe())