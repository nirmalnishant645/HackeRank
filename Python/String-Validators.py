'''
Task

You are given a string S. 
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string S.

Constraints

0 <= len(S) <= 1000

Output Format

In the first line, print True if S has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if S has any alphabetical characters. Otherwise, print False. 
In the third line, print True if S has any digits. Otherwise, print False. 
In the fourth line, print True if S has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True

'''
inputStr = input()
alnum = False
alpha = False
digit = False
lower = False
upper = False
for i in inputStr:
    if (i.isalnum()):
        alnum = True
    if (i.isalpha()):
        alpha = True
    if (i.isdigit()):
        digit = True
    if (i.islower()):
        lower = True
    if (i.isupper()):
        upper = True

print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)
