"""
Write a function check_duplicate(Lst) which returns True if a list Lst contains duplicate elements. It should return False, if all the elements in the list Lst are unique.
"""

def check_duplicate(Lst) :
    if len(Lst) == len(set(Lst)):
        return False
    else:
        return True
l=[]
n =int(input('Enter the size of list : '))
print("Enter the elemnets : ")
for i in range(0,n) :
    s=input()
    l.append(s)
if  not check_duplicate(l) :
    print("List not contains duplicates")
else :
    print("List contains duplicates")

"""
output:
Enter the size of list : 5
Enter the elemnets : 
2
5
1
4
1
List contains duplicates
"""