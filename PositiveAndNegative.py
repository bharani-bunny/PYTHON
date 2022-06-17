"""
Write a program to pass a list to a function. Calculate the total number of positive and negative numbers from the list and then display the count in terms of dictionary.
"""

def cal_pos_neg(lst) :
    n=0
    p=0
    for i in range(0,len(lst)) :
        if lst[i] < 0 :
            n=n+1
        else :
            p=p+1
    dist={'No of postive Elemeents' : p,'No of negative elements' : n}
    print(dist)

l=[]
n =int(input('Enter the size of list : '))
print("Enter the elemnets : ")
for i in range(0,n) :
    s=int(input())
    l.append(s)
cal_pos_neg(l)

"""
output :
Enter the size of list : 5
Enter the elemnets : 
2
-1
3
-9
-8
{'No of postive Elemeents': 2, 'No of negative elements': 3}
"""