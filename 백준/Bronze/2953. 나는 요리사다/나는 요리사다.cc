#include <iostream>

using namespace std;

int main() {
    int n, sum_n = 0, max_n = 0, cnt;
    for (int i = 1; i <= 5; i++) {
        sum_n = 0;
        for (int j = 0; j < 4; j++) {
            cin >> n;
            sum_n += n;
        }
        if (max_n < sum_n) {
            max_n = sum_n;
            cnt = i;
        }
    }
    cout << cnt << "\n" << max_n;
}