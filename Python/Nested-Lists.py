'''
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, N, the number of students. 
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints

2<=N<=5
There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are 5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
'''

from collections import OrderedDict

n = int(raw_input())
ar = {}
for i in range(0, n):
    tmp_name = raw_input()
    tmp_marks = float(raw_input())
    ar[tmp_name] = tmp_marks  # Entering them in the ordered dictionary

val_ar = []
for i in ar:
    tmp_val = ar[i]
    val_ar.append(tmp_val)

# print (val_ar)  --> Marks of all Students

set_val = set(val_ar)
val_ar = list(set_val)
val_ar.sort()
# print (val_ar) --> Distinct marks of students sorted in ascending order

sec_mark = val_ar[1]
final_ar = []
for i in ar:
    if (sec_mark == ar[i]):
        final_ar.append(i)

# print (final_ar) --> Array having people with second lowest marks

final_ar.sort()
for i in final_ar:
    print (i)
