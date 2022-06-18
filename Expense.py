"""
Let us assume an individual spends ‘x’ amount (in three digits) on ’Y’ item each month. The amount spent each month is stored in a file Expenses.txt in the format MonthNo:X\n. Create an application using file handling to  calculate the total amount spent on ‘Y’ item in the last six months. Consider the Expenses.txt file given below. The information contained within the file is:
Month1 : 100
Month2 : 200
Month3 : 079
Month4 : 090
Month5 : 097
Month6 : 100
Total expense in the last six months: 666
"""

fp1=open('Expenses.txt','w+')
fp1.write('Month1:100\n')
fp1.write('Month2:200\n')
fp1.write('Month3:079\n')
fp1.write('Month4:090\n')
fp1.write('Month5:097\n')
fp1.write('Month6:100\n')
print('Contents of File Expenses.txt are as follows:')
fp1.seek(0)
print(fp1.read())
fp1.seek(0)
txt = fp1.readlines()
count = 0
sum = 0
for ch in txt:
    fp1.seek(7+count)
    exp = fp1.readline().strip('\n')
    sum = sum + int(exp)
    count += 12
print('Expenses of last six month:',sum)

"""
output:
Contents of File Expenses.txt are as follows:
Month1:100
Month2:200
Month3:079
Month4:090
Month5:097
Month6:100
Expenses of last six month: 666
"""
