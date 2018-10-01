'''
Task
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 Hackos * no. of days late.
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 Hackos * no. of months late.
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.
Input Format
The first line contains space-separated integers denoting the respective day, month, and year on which the book was actually returned.
The second line contains space-separated integers denoting the respective day, month and year on which the book was expected to be returned (due date).

Constraints
1 <= D <= 31
1 <= M <= 12
1 <= Y <= 3000
It is guaranteed that dates will be valid Gregorian Calendar dates.
Output Format
Print a single integer denoting the library fine for the book received as input.

Sample Input
9 6 2015
6 6 2015

Sample Output
45
'''
return_date = [int(x) for x in input().split(' ')]
due_date = [int(x) for x in input().split(' ')]

year = 2
month = 1
day = 0

fine = 0
if return_date[year] > due_date[year]:
    fine = 10000
elif return_date[year] == due_date[year]:
    if return_date[month] > due_date[month]:
        fine = 500 * (return_date[month] - due_date[month])
    elif return_date[month] == due_date[month]:
        if return_date[day] > due_date[day]:
            fine = 15 * (return_date[day] - due_date[day])

print(fine)
