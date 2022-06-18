"""
Write a program to create a module with name Complex_Operations.py with following functions:
i) Factorial
ii) String palindrome
iii) Fibonacci series
iv) Prime number
Use this module in another program and invoke the functions that are part of it.
"""

def Factorial(n):
    f=1
    for i in range(2,n+1):
        f=f*i
    return f

def Palindrome(s):
    return s == s[::-1]

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def Prime(n):
    if n>1:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                return False
        return True
    else:
        return False
