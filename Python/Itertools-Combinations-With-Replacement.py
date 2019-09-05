'''
Task

You are given a string S.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value k separated by a space.

Constraints

0<k<=len(S)

The string contains only UPPERCASE characters.

Output Format

Print the combinations with their replacements of string S on separate lines.

Sample Input

HACK 2
Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''
from itertools import combinations_with_replacement as cwr

A, B = input().split()

C = cwr(sorted(A),int(B))

for i in C :
    print(''.join(i))
