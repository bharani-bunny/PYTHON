"""
Write a program to calculate an Internet browsing bill. Use the conditions
specified as follows:
a. 1 Hour – Rs. 20
b. 1⁄2 Hour – Rs. 10
c. Unlimited hours in a day – Rs. 100
The owner should enter the number of hours spent on browsing.
"""

a=float(input("Enter hours : "))
if(a==1):
    b=20
elif(a<1):
    b=10
else:
    b=100
print("Total bill is : ",b)

"""
output:
Enter hours : 1
Total bill is :  20
"""
