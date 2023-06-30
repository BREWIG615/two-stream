import pandas as pd

df = pd.read_csv('./data/MOCK_DATA.csv')

print(df.color.unique())