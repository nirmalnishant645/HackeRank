'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 
Your task is to determine the winner of the game and their score.

Input Format
A single line of input containing the string S. 
Note: The string S will contain only uppercase letters: [A-Z].

Output Format
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.

Question Link: https://www.hackerrank.com/challenges/the-minion-game/problem

Sample Input
BANANA

Sample Output
Stuart 12
'''

s = input().strip()
s_length = len(s)
vowel_list = ['A', 'E', 'I', 'O', 'U']

stuart_point = 0
kevin_point = 0

for i in range(s_length):
    if s[i] in vowel_list:
        kevin_point += s_length - i
    else:
        stuart_point += s_length - i
if stuart_point == kevin_point:
    print('Draw')
elif kevin_point > stuart_point:
    print('Kevin', kevin_point)
else:
    print('Stuart', stuart_point)
