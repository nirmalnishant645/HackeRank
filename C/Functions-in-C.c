/*
Task

You have to write a function int max_of_four(int a, int b, int c, int d) which reads four arguments and returns the greatest of them.

+= : Add and assignment operator. It adds the right operand to the left operand and assigns the result to the left operand.

a += b is equivalent to a = a + b;
Input Format

Input will contain four integers - a,b,c,d, one in each line.

Output Format

Print the greatest of the four integers. 
Note: I/O will be automatically handled.

Sample Input

3
4
6
5
Sample Output

6
*/

//First Way

#include <stdio.h>

int max_of_four(int a, int b, int c, int d) {
    int max1 = a > b ? a : b; // If true return a, else b
    int max2 = c > d ? c : d;
    return max1 > max2 ? max1 : max2;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

// Second Way

#include <stdio.h>

int max_of_four(int a, int b, int c, int d) {
    if (a > b) 
        if (a > c) 
            if (a > d)
            return a;
            else
            return d;
        else if (c > d)
            return c;
        else
            return d;
    else if (b > c)
        if (b > d)
            return b;
        else 
            return d;
    else
        return c;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
