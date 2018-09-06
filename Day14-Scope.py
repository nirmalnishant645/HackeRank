'''
Task 

Complete the Difference class by writing the following:

A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the maximumDifference instance variable.

Input Format

You are not responsible for reading any input from stdin. The locked Solution class in your editor reads in 2 lines of input; the first line contains N, and the second line describes the elements array.

Constraints

1<=N<=10
1<=elements[i]<=100, where 0<=i<=N-1

Output Format

You are not responsible for printing any output; the Solution class will print the value of the maximumDifference instance variable.
'''

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        
        for i in self.__elements:
            for j in self.__elements:

                diff = abs(i - j)
                
                if diff > self.maximumDifference:
                    self.maximumDifference = diff
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
