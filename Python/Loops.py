'''
Task 
Read an integer N. For all non-negative integers i<N, print i^2.

Input Format

The first and only line contains the integer, N.

Constraints
1<=N<=20

Output Format

Print N lines, one corresponding to each i.
'''

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i ** 2)
