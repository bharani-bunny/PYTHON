"""
Write programs for the following series using the while loop.
a. x+x2/2!+x3/3!+..
b. 1+x+x2+x3+....xn
"""

#a
import math
x=int(input("Enter x value : "))
n=int(input("Enter n value : "))
sum=0
i=1
while i<=n:
    sum=sum+(math.pow(x,i)/math.factorial(i))
    i=i+1;
print(sum)

"""
output:
Enter x value : 5
Enter n value : 3
38.33333333333333
"""

#b
import math
x=int(input("Enter x value : "))
n=int(input("Enter n value : "))
sum=0
i=0
while i<=n:
    sum=sum+math.pow(x,i)
    i=i+1
print(sum)

"""
Enter x value : 5
Enter n value : 3
156.0
"""