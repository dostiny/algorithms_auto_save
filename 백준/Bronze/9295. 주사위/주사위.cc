#include <iostream>

using namespace std;

int main() {
    int TC, num1, num2;
    cin >> TC;
    for (int i = 1; i <= TC; ++i) {
        cin >> num1 >> num2;
        cout << "Case " << i << ": " << num1 + num2 << "\n";
    }
}