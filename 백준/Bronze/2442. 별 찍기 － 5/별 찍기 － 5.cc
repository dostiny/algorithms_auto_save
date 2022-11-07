#include <iostream>

using namespace std;

int main() {
    int n, last;
    cin >> n;
    last = n * 2 - 1;
    char arr[last];
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n + k; ++i) {
            if (n - 1 - k <= i && i <= n - 1 + k) {
                arr[i] = '*';
            } else {
                arr[i] = ' ';
            }
            cout << arr[i];
        }
        cout << "\n";
    }
    return 0;
}