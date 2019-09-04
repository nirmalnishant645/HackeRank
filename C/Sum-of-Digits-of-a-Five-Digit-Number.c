/*
Task

In this challenge, you have to input a five digit number and print the sum of digits of the number. 

Input Format

The input contains a single five digit number, n.

Constraints

10000<=n<=99999

Output Format

Print the sum of the digits of the five digit number.

Sample Input 0

10564
Sample Output 0

16
*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n, sum=0;
    scanf("%d", &n);
    
    while(n>0) {
        sum+=n%10;
        n=floor(n/10);
    }

    printf("%d",sum);

    return 0;
}
