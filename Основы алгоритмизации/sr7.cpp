#include <iostream>
#include <string>

using namespace std;

int main() {
	string text;
	cout << "Enter string: ";
	getline(cin, text);  
	
	int count_r = 0, count_k = 0, count_t = 0;
	
	for (char ch : text) {
		if (ch == 'r' || ch == 'R') {  
			count_r++;
		} else if (ch == 'k' || ch == 'K') {
			count_k++;
		} else if (ch == 't' || ch == 'T') {
			count_t++;
		}
	}

	cout << "Count 'r': " << count_r << endl;
	cout << "Count 'k': " << count_k << endl;
	cout << "Count 't': " << count_t << endl;
	
	return 0;
}
