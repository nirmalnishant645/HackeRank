'''
Task 
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format 
The first line contains a string consisting of space separated words.

Output Format 
Print the formatted string as explained above.

Sample Input

this is a string   
Sample Output

this-is-a-string
'''
print ('-'.join(input().strip().split(' ')))
