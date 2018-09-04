'''
Task 
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

Input Format

A single integer, n.

Constraints

1<=n<=10^6

Output Format

Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.
'''

#!/bin/python3

import sys

def generate_binary(no):
    binary_string = '0' if no % 2 == 0 else '1'
    no = no // 2
    while no != 0:
         if no % 2 == 0:
           binary_string += '0'
           no = no // 2
         else:
            binary_string += '1'
            no = no // 2
    return binary_string



n = int(input().strip())
count = len(max(generate_binary(n).split('0')))
print(count)
