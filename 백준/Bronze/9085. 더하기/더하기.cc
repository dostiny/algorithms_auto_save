#include <iostream>

using namespace std;

int main() {
    int TC, n, num,sum_n;
    cin >> TC;
    for (int i = 0; i < TC; i++) {
        cin >> n;
        sum_n = 0;
        for (int j = 0; j < n; j++) {
            cin >> num;
            sum_n += num;
        }
        cout << sum_n << "\n";
    }
}