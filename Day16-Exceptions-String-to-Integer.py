'''
Task 
Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.

Note: You must use the String-to-Integer and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get a 0 score.

Input Format

A single string, S.

Constraints

1<=|S|<=6, where |S| is the length of string S.
S is composed of either lowercase letters (a-z) or decimal digits (0-9).
Output Format

Print the parsed integer value of S, or Bad String if S cannot be converted to an integer.
'''

#!/bin/python3

import sys


S = input().strip()

try:
    n = int(S)
    print(n)
except:
    print("Bad String")
