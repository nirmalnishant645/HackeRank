'''
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, n, denoting the number of commands. 
Each line i of the n subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
ar = []
n = int(input())

for i in range(0, n):
    tmp_str = raw_input()
    tmp_str_ar = tmp_str.strip().split(" ")
    cmd = tmp_str_ar[0]
    if cmd == "print":
        print(ar)
    elif cmd == "sort":
        ar.sort()
    elif cmd == "reverse":
        ar.reverse()
    elif cmd == "pop":
        ar.pop()
    elif cmd == "count":
        val = int(tmp_str_ar[1])
        ar.count(val)
    elif cmd == "index":
        val = int(tmp_str_ar[1])
        ar.index(val)
    elif cmd == "remove":
        val = int(tmp_str_ar[1])
        ar.remove(val)
    elif cmd == "append":
        val = int(tmp_str_ar[1])
        ar.append(val)
    elif cmd == "insert":
        pos = int(tmp_str_ar[1])
        val = int(tmp_str_ar[2])
        ar.insert(pos, val)
