'''
Complete the function solveMeFirst to compute the sum of two integers.

Function prototype:

int solveMeFirst(int a, int b);

where,

a is the first integer input.
b is the second integer input
Return values

sum of the above two integers
Sample Input

a = 2
b = 3
Sample Output

5
Explanation

The sum of the two integers a and b is computed as: 2+3=5.
'''

def solveMeFirst(a,b):
	# Hint: Type return a+b below
    return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
