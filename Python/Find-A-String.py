'''
Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints

1 <= len(string) <= 200
 
Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
Concept

Some string processing examples, such as these, might be useful. 
There are a couple of new concepts: 
In Python, the length of a string is found by the function len(s), where  is the string. 
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])
A range function is used to loop over some length:

range (0, 5)
Here, the range loops over 0 to 4.5  is excluded.
'''
line, target = [input() for _ in range(2)]
score = 0
for i in range(len(line)):
   if line[i:i+len(target)] == target:
        score += 1
print (score)
