'''
Task
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input Format

The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12
'''
# Method 1
m, M, n, N = [input() for i in range(4)]

print("\n".join(sorted(set(M.split())^set(N.split()),key=int)))

#Method 2
m, M, n, N = [input() for i in range(4)]

a = (set(M.split())^set(N.split()))
a = sorted(list(map(int, a)))
print (*a, sep="\n")
