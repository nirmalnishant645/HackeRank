/*
Task

This challenge requires you to print Hello, World! on a single line, and then print the already provided input string to stdout.

Note: You do not need to read any input in this challenge.

Input Format

You do not need to read any input in this challenge.

Output Format

Print Hello, World! on the first line, and the string from the given input on the second line.

Sample Input 0

Welcome to C programming.
Sample Output 0

Hello, World!
Welcome to C programming.
*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
	
    char s[100];
    scanf("%[^\n]%*c", &s);
  	
    printf("Hello, World!\n%s",s);   
    return 0;
}
