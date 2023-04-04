import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df=pd.DataFrame(exam_data,index=['서준','우현','민아'])

print(df)
print()

print(df.iloc[::-1])
'''
music_gym=df[['음악','체육']]

print(music_gym)
print(type(music_gym))
print()

math2=df[['수학']]
print(math2)
print(type(math2))
'''