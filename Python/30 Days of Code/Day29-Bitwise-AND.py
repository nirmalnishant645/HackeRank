'''
Task
Given set S. Find two integers, A and B (where A < B), from set S such that the value of A&B is the maximum possible and also less than a given integer, K. In this case, & represents the bitwise AND operator.

Input Format
The first line contains an integer, T, the number of test cases. Each of the T subsequent lines defines a test case as 2 space-separated integers, N and K, respectively.

Output Format
For each test case, print the maximum possible value of on a new line.

Sample Input
3 5 2 8 5 2 2

Sample Output
1 4 0
'''

T = int(input())

for i in range(T):
    tmp = str(input()).split()
    N = int(tmp[0])
    K = int(tmp[1])

    maximum = 0

    for j in range(1, N):
        for k in range(j + 1, N + 1):
            h = j & k
            if K > h > maximum:
                maximum = h

    print(maximum)
