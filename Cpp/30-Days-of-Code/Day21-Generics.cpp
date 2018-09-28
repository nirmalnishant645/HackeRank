/*
Task:
Write a single generic function named printArray; this function must take an array of generic elements as a parameter (the exception to this is C++, which takes a vector). The locked Solution class in your editor tests your function.

Note: You must use generics to solve this challenge. Do not write overloaded functions.

Input Format
There is no input for this challenge. The locked Solution class in your editor will pass two different types of arrays to your printArray function.

Constraints
You must have exactly 1 function named printArray.

Output Format
Your printArray function should print each element of its generic array parameter on a new line.
*/
#include <iostream>
#include <vector>
#include <string>

using namespace std;
template <typename t>
void printArray (vector<t> v_) {
    for (auto &element : v_) {
        cout << element << endl;
    }
}
int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}
