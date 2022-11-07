#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) { // ex) num=5일때 i = 0 1 2 3 4
        for (int j = 0; j < n - i; j++) cout << " ";
        for (int k = 0; k <2*i -1; k++) cout << "*";
        cout << '\n';
    }

    for (int i = 1; i < n; i++) { //i=1 2 3 4
        for (int j = 0; j < i; j++) cout << " "; // j=0 01 012 0123
        for (int k = 0; k < 2 * n - (2 * i + 1); k++) cout << "*";
        cout << "\n";
    }
}