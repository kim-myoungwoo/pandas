import pandas as pd

student1 = pd.Series({'국어':100,'영어':80,'수학':90})
student2 = pd.Series({'수학':80,'국어':90,'영어':100})
'''
print(student1)
print()
print(student2)
print()
'''
addition=student1 +student2
subtraction=student1-student2

result=pd.DataFrame([addition,subtraction],index=['덧셈','뺄셈'])
print(result)


'''
percentage=student1/200

print(percentage)
print(type(percentage))
'''