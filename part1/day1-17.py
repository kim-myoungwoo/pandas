import pandas as pd
import seaborn as sns

titanic=sns.load_dataset('titanic')


df=titanic.loc[:,['age','fare']]
print(df.head())

print()

addtion=df+10
print(addtion.head())