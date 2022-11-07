#include <iostream>

using namespace std;

int main() {
    int n, tap, result = 0;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> tap;
        result += tap;
    }
    cout << result - (n - 1);
}