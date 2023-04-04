import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])

print(df)

#print(df.index)
#print(df.columns)
print("----------------------------")

df.rename(columns={'나이':'연령'},inplace=True)
df.rename(columns={'준서':'학생1'},inplace=True)

print(df)



'''
df.index=['학생1','학생2']
df.columns=['연령','남녀','소속']

print(df)
print(df.index)
print(df.columns)'''

