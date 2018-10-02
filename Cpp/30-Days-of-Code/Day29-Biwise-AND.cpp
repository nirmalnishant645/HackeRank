/*
Task
Given set S. Find two integers, A and B (where A < B), from set S such that the value of A&B is the maximum possible and also less than a given integer, K. In this case, & represents the bitwise AND operator.
Input Format
The first line contains an integer, T, the number of test cases. Each of the T subsequent lines defines a test case as 2 space-separated integers, N and K, respectively.
Output Format
For each test case, print the maximum possible value of on a new line.
Sample Input
3 
5 2 
8 5 
2 2
Sample Output
1 
4 
0
*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{    
 int T, n, k, i, j, val;
 cin>>T;
    
 while(T>0)
    {    
        int maximum = 0;
        cin>>n>>k;
        
        for (i=1;i<n-1;i++) 
 {
            for (j=i+1;j<=n;j++) 
 {
                val=i&j;
                           
 if (val>maximum&&val<k) 
                    maximum = val;                    
            }    
        }
            cout<<maximum<<endl;
        T--;
    }
 return 0;
}
