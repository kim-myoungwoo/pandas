import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df=pd.DataFrame(exam_data,index=['서준','우현','민아'])

#print(df)
#print()
'''
df2 =df[:]

df2=df2.drop('우현')

print(df2)
'''
df3 = df[:]

df3=df3.drop(['우현','민아'])

print(df3)

