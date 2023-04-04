import pandas as pd

exam_data = {'이름':['서준','우현','민아'],
             '수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df=pd.DataFrame(exam_data)

print(df)
print()
ndf=df.set_index(['이름'])
print(ndf)
print()

ndf3=ndf.set_index(['수학','음악'])

print(ndf3)

'''
ndf2=ndf.set_index(['음악'])

print(ndf2)
print()
'''