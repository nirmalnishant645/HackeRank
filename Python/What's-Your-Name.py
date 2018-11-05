'''
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

Input Format

The first line contains the first name, and the second line contains the last name.

Constraints

The length of the first and last name ≤ 10.

Output Format

Print the output as mentioned above.

Sample Input 0

Ross
Taylor
Sample Output 0

Hello Ross Taylor! You just delved into python.
Explanation 0

The input read by the program is stored as a string data type. A string is a collection of characters.

'''
print ("Hello {0} {1}! You just delved into python.".format(raw_input(), raw_input()))
