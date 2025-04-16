#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int N;
	double number, product = 1.0;
	
	cout << "Enter the number of elements (N): ";
	cin >> N;
	
	if (N <= 0) {
		cout << "Error: The number of elements must be positive." << endl;
		return 1;
	}
	
	ofstream outFile("numbers.txt");
	if (!outFile) {
		cout << "Error: Unable to open the file for writing." << endl;
		return 1;
	}
	
	cout << "Enter " << N << " real numbers:" << endl;
	for (int i = 0; i < N; i++) {
		cin >> number;
		outFile << number << " "; 
	}
	outFile.close();
	
	ifstream inFile("numbers.txt");
	if (!inFile) {
		cout << "Error: Unable to open the file for reading." << endl;
		return 1;
	}
	
	while (inFile >> number) {
		product *= number; 
	}
	inFile.close();
	
	cout << "Product of numbers: " << product << endl;
	
	return 0;
}
