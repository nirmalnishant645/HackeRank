'''
Task 
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input Format

The first line contains an integer, T (the number of test cases). 
Each line i of the T subsequent lines contain a String, S.

Constraints
1<=T<=10
2<=Length of S<=10000

Output Format

For each String S<j> (where 0<=j<=T-1), print S<j>'s even-indexed characters, followed by a space, followed by S<j>'s odd-indexed characters.
'''
n = int(input())
for i in range(n):
    s = input()
    s1 = list(s)
    l = len(s1)
    odd = ''
    even = ''
    for i in range(0,l):
        if i%2 == 0:
            even += str(s1[i])
        else:
            odd += str(s1[i])
    print (even, odd)
