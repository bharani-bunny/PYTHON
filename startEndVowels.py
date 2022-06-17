"""
Write the function startEndVowels(word) which returns True if the word starts and ends with vowels.
"""

def startEndVowels(word):
    s="AaEeIiOoUu"
    if s.__contains__(word[0]) and s.__contains__(word[-1]) :
        return True
    else :
        return False
s=input("Enter a word : ")
if startEndVowels(s):
    print("Given word ",s,"starts and ends with Vowel")
else :
    print("Given word ", s, "not starts and ends with Vowel")

"""
output:
Enter a word : India
Given word  India starts and ends with Vowel
"""