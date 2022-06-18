"""
Write a program to handle the exceptions in Python using five keywords try, except, else, finally, and raise. (Note: Handle atleast three inbuilt exceptions)
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
finally:
    print("Program excecuted succesfully")

"""
output:
Enter the salary : 48000
Salary is in the range (5000,50000)
Program excecuted succesfully
"""