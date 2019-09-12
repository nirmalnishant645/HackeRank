'''
Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in MM DD YYY format.

Constraints

2000 < year < 3000

Output Format

Output the correct day in capital letters.

Sample Input

08 05 2015
Sample Output

WEDNESDAY
'''

Calendar Moduleimport calendar

mm, dd, yyyy =  input().split()
days = list()

for day in calendar.Calendar().itermonthdays(int(yyyy), int(mm)): 
    days.append(day)

n = days.index(int(dd))
n%=7

print((calendar.day_name[n-1]).upper())
