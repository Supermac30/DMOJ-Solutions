/*
  https://dmoj.ca/problem/cco98p1
*/
#include <iostream>
#include <map>
#include <string>

using namespace std;

string add(string b, string a) {
	// a<b
	string total = "";
	int carry = 0;
	int answer;
	while (b.size() > a.size()) {
		a = "0"+a;
	}
	for (unsigned long int i = 0; i < a.size(); i++) {
		answer = a.at(a.size()-i-1)+b.at(a.size()-i-1) - 96 + carry;
		carry = answer/10;
		total = to_string(answer%10) + total;
	}
	if (carry != 0) {
		total = to_string(carry)+total;
	}
	return total;
}

map<int, string> fibs;
int main() {
	fibs[1] = "1";
	fibs[2] = "1";
	for (int i = 3; i <= 200; i++) {
		fibs[i] = add(fibs.at(i-1), fibs.at(i-2));
	}

	int out;
	scanf("%i", &out);
	while (out != 0) {
		cout << fibs[out] << endl;
		scanf("%i", &out);	
	}
	return 0;
}
