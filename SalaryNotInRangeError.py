"""
Write a program to create a customized exception SalaryNotInRangeError. If the input salary is not be in the range 5000 and 50000, raise the exception otherwise display the employee salary.
"""

class SalaryNotInRangeError(Exception):
    def __init__(self, s):
        self.s = s
    pass


sal = eval(input("Enter the salary : "))
try:
    if not 5000 < sal < 50000:
        raise SalaryNotInRangeError(sal)
except:
    print("Salar is not in the range (5000,50000)")
else:
    print("Salary is in the range (5000,50000)")

"""
output:
Enter the salary : 1000
Salar is not in the range (5000,50000)
"""