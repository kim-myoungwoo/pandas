import pandas as pd
import seaborn as sns

titanic=sns.load_dataset('titanic')


df=titanic.loc[:,['age','fare']]

print(df.tail())
print()
addtion=df+10

print(addtion.tail())
print()

subtraction=addtion-df
print(subtraction.tail())