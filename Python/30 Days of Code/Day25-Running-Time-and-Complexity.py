'''
Task
A prime is a natural number greater 1 than that has no positive divisors other than 1 and itself. Given a number, n, determine and print whether it's Prime or Not Prime.

Note: If possible, try to come up with a O(sqrt(n)) primality algorithm, or see what sort of optimizations you come up with for an O(n) algorithm. Be sure to check out the Editorial after submitting your code!

Input Format
The first line contains an integer, T, the number of test cases. Each of the T subsequent lines contains an integer, n, to be tested for primality.

Constraints
1 <= T <= 20
1 <= n <= 2 x 10 9
Output Format
For each test case, print whether n is Prime or Not Prime on a new line.

Sample Input
3
12
5
7

Sample Output
Not prime
Prime
Prime
'''
import math

def is_prime(n):
    root = n**.5
    upper = int(math.floor(root) + 1)

    if n == 1:
        return False
    
    elif n == 2:
        return True

    if n % 2 == 0:
        return False

    for div in range(3, upper, 2):
        if n % div == 0:
            return False
    else:
        return True

T = int(input())
for i in range(T):
    data = int(input())
    if is_prime(data):
        print("Prime")
    else:
        print("Not prime")
