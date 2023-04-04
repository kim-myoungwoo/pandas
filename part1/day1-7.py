import pandas as pd

exam_data = {'이름':['서준','우현','민아'],
             '수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df=pd.DataFrame(exam_data)

#print(df)
#print()
df.set_index('이름',inplace=True)

print(df)
print()

j=df.iloc[0:2,2:]

print(j)

'''
i=df.loc['서준':'우현','음악':'체육']
print(i)

h= df.iloc[[0,1],[2,3]]
print(h)

g=df.loc[['서준','우현'],['음악','체육']]
print(g)

f=df.iloc[0,2:]
print(f)

e=df.loc['서준','음악':'체육']
print(e)

d=df.iloc[0,[2,3]]

print(d)
print(type(d))

c=df.loc['서준',['음악','체육']]
print()
print(c)
print(type(c))

a=df.loc['서준','음악']
print(a)
print()
b=df.iloc[0,2]
print(b)
'''