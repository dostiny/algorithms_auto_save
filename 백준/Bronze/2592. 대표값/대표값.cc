#include <iostream>

using namespace std;

int arr[102];

int main() {
    int n, sum_n = 0, max_v = 0, max_i = 0;
    for (int i = 1; i <= 10; i++) {
        cin >> n;
        arr[n/10]++;
        sum_n += n;
    }
    for (int i = 1; i <= 100; i++) {
        if (max_i < arr[i]) {
            max_v = i * 10;
            max_i = arr[i];
        }
    }
    cout << sum_n / 10 << "\n" << max_v << "\n";
}