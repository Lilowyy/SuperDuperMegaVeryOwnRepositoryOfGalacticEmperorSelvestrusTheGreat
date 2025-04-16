#include <iostream>
#include <string>

using namespace std;

struct Student {
	string full_name; 
	string student_id; 
	int grades[4]; 
	
	double average_grade() const {
		double sum = 0;
		for (int i = 0; i < 4; i++) {
			sum += grades[i];
		}
		return sum / 4;
	}
	
	string category() const {
		bool all_5 = true, all_4 = true, all_3 = true;
		for (int i = 0; i < 4; i++) {
			if (grades[i] != 5) all_5 = false;
			if (grades[i] < 4) all_4 = false;
			if (grades[i] < 3) all_3 = false;
		}
		if (all_5) return "epic";
		if (all_4) return "good";
		if (all_3) return "not bad";
		return "bad";
	}
};

void sort_by_name(Student students[], int size) {
	for (int i = 0; i < size - 1; i++) {
		for (int j = 0; j < size - i - 1; j++) {
			if (students[j].full_name > students[j + 1].full_name) {
				swap(students[j], students[j + 1]);
			}
		}
	}
}

void sort_by_average_grade(Student students[], int size) {
	for (int i = 0; i < size - 1; i++) {
		for (int j = 0; j < size - i - 1; j++) {
			if (students[j].average_grade() < students[j + 1].average_grade()) {
				swap(students[j], students[j + 1]);
			}
		}
	}
}

void print_students(Student students[], int size) {
	for (int i = 0; i < size; i++) {
		cout << students[i].full_name << " (" << students[i].student_id << "): ";
		for (int j = 0; j < 4; j++) {
			cout << students[i].grades[j] << " ";
		}
		double avg = students[i].average_grade();
		cout << ", avg: " << (int)(avg * 100 + 0.5) / 100.0 << endl;
	}
}

void find_students_by_category(Student students[], int size, const string& category) {
	bool found = false;
	for (int i = 0; i < size; i++) {
		if (students[i].category() == category) {
			cout << "  " << students[i].full_name << " (" << students[i].student_id << ")" << endl;
			found = true;
		}
	}
	if (!found) {
		cout << "  no this students" << endl;
	}
}

int main() {
	const int group_size = 5;
	Student group[group_size] = {
		{"Ivanov", "001", {5, 5, 5, 5}},
		{"Petrov", "002", {4, 4, 4, 4}},
		{"Sidorov", "003", {3, 3, 3, 3}},
		{"Kuznec", "004", {2, 3, 3, 5}},
		{"Morozov", "005", {2, 2, 2, 2}}
	};
	
	Student sorted_by_name[group_size];
	for (int i = 0; i < group_size; i++) {
		sorted_by_name[i] = group[i];
	}
	sort_by_name(sorted_by_name, group_size);
	
	cout << "List of students:" << endl;
	print_students(sorted_by_name, group_size);
	
	Student sorted_by_grade[group_size];
	for (int i = 0; i < group_size; i++) {
		sorted_by_grade[i] = group[i];
	}
	sort_by_average_grade(sorted_by_grade, group_size);
	
	cout << "\nList of students for decrease avg:" << endl;
	print_students(sorted_by_grade, group_size);
	
	double total_grades = 0;
	for (int i = 0; i < group_size; i++) {
		for (int j = 0; j < 4; j++) {
			total_grades += group[i].grades[j];
		}
	}
	double group_average = total_grades / (group_size * 4);
	
	cout << "\navg group: " << (int)(group_average * 100 + 0.5) / 100.0 << endl;
	
	string categories[] = {"epic", "good", "not bad", "bad"};
	for (const string& category : categories) {
		cout << "\n" << category << ":" << endl;
		find_students_by_category(group, group_size, category);
	}
	
	return 0;
}
