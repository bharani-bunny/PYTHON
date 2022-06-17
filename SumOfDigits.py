"""
A four-digit integer is entered through the keyboard. Write a function to calculate the sum of the four-digit number both without recursion and using recursion.
"""

#without recursion
l=[]
b=int(input("Enter a number: "))
while(b>0):
    dig=b%10
    l.append(dig)
    b=b//10
print("Sum is:")
print(sum(l))

"""
output:
Enter a number: 1234
Sum is:
10
"""

#with recursion
def sumo( n ):
    if n == 0:
        return 0
    return (n % 10 + sumo(int(n / 10)))
num = int(input("Enter a number : "))
r=sumo(num)
print("Sum of digit is ", r)

"""
output:
Enter a number : 1234
Sum of digit is  10
"""