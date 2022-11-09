#include <iostream>

using namespace std;

int main() {
    int max_n = 0, n, arr[9];
    for (int i = 0; i < 9; i++) {
        cin >> arr[i];
        if (max_n < arr[i]) {
            max_n = arr[i];
            n = i + 1;
        }
    }
    cout << max_n << "\n" << n;
}