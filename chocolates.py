"""
Consider a scenario where a son eats five chocolates every day. The price of  each chocolate is different. His father pays the bill to the chocolate vendor at  the end of every week. Develop a program that can generate the bills for the  chocolates and send to the father. Also state which loop will be used to solve  this problem
"""

sum = 0
for i in range (1,8):
    print("Enter total money spent by son in day ",i,": ")
    n = int(input())
    sum = sum + n
print("Total money to be paid : ",sum);

"""
output:
Enter total money spent by son in day  1 : 
23
Enter total money spent by son in day  2 : 
21
Enter total money spent by son in day  3 : 
45
Enter total money spent by son in day  4 : 
32
Enter total money spent by son in day  5 : 
56
Enter total money spent by son in day  6 : 
43
Enter total money spent by son in day  7 : 
45
Total money to be paid :  265
"""