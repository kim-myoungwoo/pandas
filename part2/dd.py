import pandas as pd

df1=pd.read_excel('./남북한발전전력량.xlsx',engine='openpyxl')

print(df1)

df2=pd.read_excel('./남북한발전전력량.xlsx',engine='openpyxl', header=None)

print(df2)