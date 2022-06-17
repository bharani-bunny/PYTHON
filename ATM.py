"""
An ATM contains Indian currency notes of 100, 500 and 1000. To withdraw cash from this ATM, the user has to enter the number of notes he/she wants of each currency, i.e. of 100, 500 and 1000. Write a program to calculate the total amount withdrawn by the person from the ATM in rupees.
"""

num_100 = int (input ("Enter number of 100 notes :"))
num_500 = int (input ("Enter number of 500 notes: "))
num_1000 = int (input ("Enter number of 1000 notes: "))
print ("Total Amount withdracn is : ",(num_100 * 100.0 + num_500 * 500.0 + num_1000 * 1000.0))

"""
output:
Enter number of 100 notes :3
Enter number of 500 notes: 1
Enter number of 1000 notes: 2
Total Amount withdracn is :  2800.0
"""