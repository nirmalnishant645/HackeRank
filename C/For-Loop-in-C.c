/*
Task

For each integer n in the interval [a,b] (given as input) :

If 1<=n<=9, then print the English representation of it in lowercase. That is "one" for 1, "two" for 2, and so on.
Else if n>9 and it is an even number, then print "even".
Else if n>9 and it is an odd number, then print "odd".
Input Format

The first line contains an integer, a. 
The seond line contains an integer, b.

Constraints

1<=a<=b<=10^6

Output Format

Print the appropriate english representation,even, or odd, based on the conditions described in the 'task' section.

Note: [a,b] = {x ∈ Z | a<=x<=b} = {a,a+1,...,b}

Sample Input

8
11
Sample Output

eight
nine
even
odd
*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b, li;
    scanf("%d\n%d", &a, &b);
    
    char *l[11] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "even", "odd"};

    for (int i=a; i<=b; i++) {
        li = i <= 9 ? i - 1 : 9 + i % 2;
        printf("%s\n", l[li]);
    }

    return 0;
}
