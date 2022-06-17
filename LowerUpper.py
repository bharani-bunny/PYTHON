"""
Write a program to read string and display ‘Total number of uppercase and lowercase letters’.
"""

s=input("Enter a string : ")
u=0
l=0
for i in s:
    if(i.isupper()):
        u=u+1
    elif(i.islower()):
        l=l+1
print("Lower count : ",l)
print("Upper count : ",u)

"""
output:
Enter a string : Bharani
Lower count :  6
Upper count :  1
"""