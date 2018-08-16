'''
Task 
Given an integer, n, print its first 10 multiples. Each multiple n x i (where 1<=i<=10) should be printed on a new line in the form: n x i = result.

Input Format

A single integer, n.

Constraints
2<=n<=20

Output Format

Print 10 lines of output; each line i (where 1<=i<=10) contains the result of n x i in the form: 
n x i = result.
'''
import sys

n = int(input().strip())

for i in range(1, 11):
    a = str(n) + ' x ' + str(i) + ' = ' + str(n*i)
    sys.stdout.write (a + '\n')
