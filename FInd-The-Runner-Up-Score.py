'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.
Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
Output Format
Print the runner-up score.
Sample Input:
5
2 3 6 6 5
Sample Output:
5
'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max = arr[0]
    res = -101
    index = 1
    while index < len(arr):
        if (arr[index] != res and arr[index] != max):
            if arr[index] > max:
                res = max
                max = arr[index]
            elif arr[index] > res:
                res = arr[index]
        index += 1
    print(res)
