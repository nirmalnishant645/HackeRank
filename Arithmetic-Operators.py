'''
Task 
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Input Format

The first line contains the first integer, . The second line contains the second integer, .

Constraints

1<=a<=10^10
1<=b<=10^10

Output Format

Print the three lines as explained above.
'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print((a + b), (a - b), (a * b), sep='\n')
