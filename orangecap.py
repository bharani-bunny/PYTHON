"""
Define a Python function 'orangecap(d)' which reads a dictionary 'd' of the following form and identifies the player with the highest total score. The function should return a pair (playername, topscore), where playername is the name of the player with the highest score and topscore is the total runs scored by the player.
Input
orangecap({'test1':{'Dhoni':74, 'Kohli':150}, 'test2':{'Dhoni':29,
'Pujara':42}})
Output
('Kohli', 150)
"""

def orangecap(d):
    total = {}
    for k in d.keys():
        for n in d[k].keys():
            if n in total.keys():
                total[n] = total[n] + d[k][n]
            else:
                total[n] = d[k][n]
    print('Total Run Scored by Each Player in 2 Tests: ')
    print(total)
    print('Player With Highest Score')
    maxtotal = -1
    for n in total.keys():
        if total[n] > maxtotal:
            maxname = n
            maxtotal = total[n]
    return(maxname,maxtotal)
d=orangecap({'test1':{'Dhoni':74, 'Kohli':150}, 'test2':{'Dhoni':29, 'Pujara':42}})
print(d)

"""
output:
Total Run Scored by Each Player
{'Dhoni': 103, 'Pujara': 42, 'Kohli': 150}
Player With Highest Score
('Kohli', 150)
"""
