"""
Write a function Calc_GCD_Recurr(a, b) which calculates the GCD
recursively of two numbers. The function should take two positive integers
and should return one integer as GCD.
"""

def Calc_GCD_Recurr(a,b):
    if(b==0):
        return a
    else:
        return Calc_GCD_Recurr(b,a%b)
a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))
print("The gcd is ",Calc_GCD_Recurr(a,b))

"""
output:
Enter value of a : 80
Enter value of b : 45
The gcd is  5
"""