'''
Write a function to return minimum and maximum in an array.
Your program should make the minimum number of comparisons. 
'''

'''
METHOD 1 (Simple Linear Search) 

Initialize values of min and max as minimum and maximum of the first two elements respectively.
Starting from 3rd, compare each element with max and min, and change max and min accordingly
(i.e., if the element is smaller than min then change min,
else if the element is greater than max then change max, else ignore the element) 

Time Complexity: O(n)
'''

