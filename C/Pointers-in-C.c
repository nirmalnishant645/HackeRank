/*
Task

You have to complete the function void update(int *a,int *b), which reads two integers as argument, and sets  with the sum of them, and b with the absolute difference of them.
a' = a + b
b' = |a - b|

Input Format

The input will contain two integers, a and b, separated by a newline.

Output Format

You have to print the updated value of a and b, on two different lines.

Note: Input/ouput will be automatically handled. You only have to complete the function described in the 'task' section.

Sample Input

4
5
Sample Output

9
1
*/
#include <stdio.h>

void update(int *a,int *b) {
    int temp = *a;
    *a = (*a)+(*b);
    *b = abs((temp)-(*b));     
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

