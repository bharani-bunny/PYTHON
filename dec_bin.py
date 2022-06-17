"""
Write a program to define function dec_bin(num) to convert the existing decimal number into its equivalent binary number.
"""

def dec_bin(n):
    if n >= 1:
        dec_bin(n // 2)
    print(n % 2, end = '')
n = int(input("Enter a number: "))
dec_bin(n)

"""
output:
Enter a number: 15
01111
"""