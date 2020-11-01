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

# Structure is used to return two values from minMax()
class pair:
    def __init__(self):
        self.min = 0
        self.max = 0
 
def getMinMax(arr: list, n: int) -> pair:
    minmax = pair()
 
    # If there is only one element then return it as min and max both
    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax
 
    # If there are more than one elements, then initialize min and max
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]
 
    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
 
    return minmax
 
# Driver Code
if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = len(arr)
    minmax = getMinMax(arr, arr_size)
    print('Simple Linear Search: ')
    print("Minimum element is: ", minmax.min)
    print("Maximum element is: ", minmax.max)



'''
METHOD 2 (Tournament Method) 
Divide the array into two parts and compare the maximums and minimums of the two parts to get the maximum and the minimum of the whole array.

Pair MaxMin(array, array_size)
   if array_size = 1
      return element as both max and min
   else if arry_size = 2
      one comparison to determine max and min
      return that pair
   else    /* array_size  > 2 */
      recur for max and min of left half
      recur for max and min of right half
      one comparison determines true max of the two candidates
      one comparison determines true min of the two candidates
      return the pair of max and min

Time Complexity: O(n) 
'''

# Python program of above implementation
def getRecMinMax(low, high, arr):
    arr_max = arr[low]
    arr_min = arr[low]
     
    # If there is only one element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)
         
    # If there is only two element
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)
    else:
         
        # If there are more than 2 elements
        mid = int((low + high) / 2)
        arr_max1, arr_min1 = getRecMinMax(low, mid, arr)
        arr_max2, arr_min2 = getRecMinMax(mid + 1, high, arr)
 
    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))
 
# Driver code
arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
print('Tournament Method: ')
arr_max, arr_min = getRecMinMax(low, high, arr)
print('Minimum element is: ', arr_min)
print('nMaximum element is: ', arr_max)

