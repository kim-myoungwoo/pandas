import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df=pd.DataFrame(exam_data,index=['서준','우현','민아'])

print(df)
print()

label3=df.loc['서준':'우현']
position3=df.iloc[0:2]

print(label3)
print()
print(position3)


'''
label2=df.loc[['서준','우현']]

position2=df.iloc[[0,1]]

print(label2)
print(type(label2))
print("---------------------------")
print(position2)
print(type(position2))
'''
'''
label1=df.loc['서준']
print(label1)
print(type(label1))

position1=df.iloc[0]
print(position1)
print(type(position1))
'''