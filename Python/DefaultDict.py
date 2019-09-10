'''
Task
In this challenge, you will be given 2 integers, n and m. There are  words, which might repeat, in word group A. 
There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Constraints

1<=n<=10000
1<=m<=100
1<=length of each word in the input<=100

Input Format

The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group .
The next m lines contains the words belonging to group .

Output Format

Output m lines.
The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.

Sample Input

5 2
a
a
b
a
b
a
b
Sample Output

1 2 4
3 5
'''
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(lambda: -1)

for i in range(1, n+1): 
    word = input()
    d[word] = d[word] + ' ' + str(i) if word in d else str(i)

for j in range(m):
    print(d[input()])
