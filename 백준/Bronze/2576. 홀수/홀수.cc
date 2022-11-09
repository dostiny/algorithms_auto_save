#include <iostream>

using namespace std;

int main() {
    int n, sum_n = 0, min_n = 101, cnt = 0;
    for (int i = 0; i < 7; i++) {
        cin >> n;
        if (n % 2) {
            cnt++;
            sum_n += n;
            if (min_n > n) min_n = n;
        }
    }
    if (cnt) cout << sum_n << "\n" << min_n;
    else cout << -1;
}