'''
Task

You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value k separated by a space.

Constraints

0<k<=len(S)

The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string S on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
'''
from itertools import combinations

A, B = input().split()

for i in range(1,int(B)+1):
    for j in list(combinations(sorted(A), i)):
        print(''.join(j))
