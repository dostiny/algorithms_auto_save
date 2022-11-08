#include <iostream>

using namespace std;

int main() {
    int n, result = 0;
    cin >> n;
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= i; ++j) {
            result += 1;
        }
    }
    cout << result * n;
}