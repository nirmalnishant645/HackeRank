/*
Task

You have to print the character, ch, in the first line. Then print s in next line. In the last line print the sentence, sen.

Input Format

First, take a character, ch as input. 
Then take the string, s as input. 
Lastly, take the sentence sen as input.

Output Format

Print three lines of output. The first line prints the character, ch. 
The second line prints the string, s. 
The third line prints the sentence, sen.

Sample Input 0

C
Language
Welcome To C!!
Sample Output 0

C
Language
Welcome To C!!
*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX_LEN 128

int main() 
{

    char ch, word[MAX_LEN], sen[MAX_LEN];

    scanf("%c\n%s\n%[^\n]%*c",&ch,&word,&sen);

    printf("%c\n%s\n%s",ch,word,sen);

    return 0;
}
