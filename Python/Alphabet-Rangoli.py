'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

Input Format

Only one line of input containing N, the size of the rangoli.

Constraints

0 < N < 27

Output Format

Print the alphabet rangoli in the format explained above.

Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''
n = int(input().strip())
w = (n-1) * 2 + ((n * 2) - 1)
# upper half

for i in range(1, n):
    number_of_letter = (i * 2) - 1
    #print ("number of letters ", number_of_letter)
    s = ''
    letter_value = 97 + n - 1
    #print ("letter_value ", letter_value)

    for j in range(0, number_of_letter):
        if j != 0:
            s += '-'
        s += chr(letter_value)
        if j < (number_of_letter - 1) / 2:
            letter_value -= 1
        else:
            letter_value += 1

    print(s.center(w, '-'))

# bottom half

for i in range(n, 0, -1):
    number_of_letter = (i * 2) - 1
    s = ''
    letter_value = 97 + n - 1
    for j in range(0, number_of_letter):
        if j != 0:
            s += '-'
        s += chr(letter_value)
        if j < (number_of_letter-1) / 2:
            letter_value -= 1
        else:
            letter_value += 1
    print (s.center(w, '-'))
